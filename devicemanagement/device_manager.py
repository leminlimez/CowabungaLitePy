import os
import sys
import traceback
from pathlib import Path
from shutil import copytree, rmtree

from PySide6.QtCore import QStandardPaths, QCoreApplication
from PySide6.QtWidgets import QMessageBox

from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.mobilebackup2 import Mobilebackup2Service

from devicemanagement.constants import Device, Version
from devicemanagement.data_singleton import DataSingleton
from devicemanagement.create_backup import create_backup

class DeviceManager:
    last_tested_version: Version = Version("17.4")
    min_version: Version = Version("15")

    ## Class Functions
    def __init__(self):
        self.devices: list[Device] = []
        self.data_singleton = DataSingleton()
        self.current_device_index = 0
    
    def get_devices(self, network: bool = False):
        if (network):
            print("ERROR: NOT IMPLEMENTED")
            return
        self.devices.clear()
        connected_devices = usbmux.list_devices()
        # Connect via usbmuxd
        for device in connected_devices:
            try:
                ld = create_using_usbmux(serial=device.serial)
                vals = ld.all_values
                is_ipad: bool = 'iPhone' not in vals['DeviceClass']
                dev = Device(uuid=device.serial, name=vals['DeviceName'], version=vals['ProductVersion'], ipad=is_ipad)
                ## TODO: ADD CHECKS TO MAKE SURE THE DEVICE IS ACTUALLY CONNECTED
                self.devices.append(dev)
            except:
                print(f"ERROR with lockdown device with UUID {device.serial}")
        
        if len(connected_devices) > 0:
            self.set_current_device(index=0)
        else:
            self.set_current_device(index=None)

    ## CURRENT DEVICE
    def set_current_device(self, index: int = None):
        if index == None:
            self.data_singleton.current_device = None
            self.data_singleton.current_workspace = None
            self.data_singleton.device_available = False
            self.current_device_index = 0
        else:
            self.data_singleton.current_device = self.devices[index]
            if Version(self.devices[index].version) < DeviceManager.min_version:
                self.data_singleton.device_available = False
            else:
                self.data_singleton.device_available = True
                self.setup_workspace(uuid=self.devices[index].uuid)
            self.current_device_index = index
        
    def get_current_device_name(self) -> str:
        if self.data_singleton.current_device == None:
            return "No Device"
        else:
            return self.data_singleton.current_device.name
        
    def get_current_device_version(self) -> str:
        if self.data_singleton.current_device == None:
            return ""
        else:
            return self.data_singleton.current_device.version
    
    def get_current_device_uuid(self) -> str:
        if self.data_singleton.current_device == None:
            return ""
        else:
            return self.data_singleton.current_device.uuid

    def setup_workspace(self, uuid: str):
        # create the workspace for the uuid
        app_data_dir = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        path: Path = Path(app_data_dir).joinpath("CowabungaLiteData").joinpath("Workspace").joinpath(uuid)
        print(f"path here: {path}")
        path.mkdir(parents=True, exist_ok=True)
        # Copy subfolders of files into path if not there
        # TODO: Only copy if it was updated
        source_dir: str
        if QCoreApplication.applicationName() == "Python":
            source_dir = os.path.join(os.getcwd(), "file_folders/files")
        else:
            source_dir = os.path.join(sys._MEIPASS, "file_folders/files")
        copytree(src=source_dir, dst=path, dirs_exist_ok=True)
        self.data_singleton.current_workspace = path

    
    ## APPLYING TWEAKS AND RESTORING
    def apply_tweaks(self, update_label=lambda x: None, update_bar=lambda y: None):
        ws = self.data_singleton.current_workspace

        # TODO: Apply Theming

        # Copy enabled tweaks
        update_label("Copying enabled tweaks...")

        # Erase backup folder
        enabled_tweaks_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)).joinpath("CowabungaLiteData").joinpath("EnabledTweaks")
        rmtree(enabled_tweaks_dir, ignore_errors=True)

        # Copy enabled tweak files
        for tweak in self.data_singleton.enabled_tweaks:
            folder_path = Path(ws).joinpath(tweak.name)
            copytree(src=folder_path, dst=enabled_tweaks_dir, dirs_exist_ok=True)

        self.generate_and_restore(update_label, update_bar)

    ## REMOVING TWEAKS
    def remove_tweaks(self, deep_clean: bool, update_label=lambda x: None, update_bar=lambda y: None):
        source_dir: str
        if QCoreApplication.applicationName() == "Python":
            source_dir = os.path.join(os.getcwd(), "file_folders")
        else:
            source_dir = os.path.join(sys._MEIPASS, "file_folders")
        if deep_clean:
            source_dir = os.path.join(source_dir, 'restore-deepclean')
        else:
            source_dir = os.path.join(source_dir, 'restore')

        # Erase backup folder
        enabled_tweaks_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)).joinpath("CowabungaLiteData").joinpath("EnabledTweaks")
        rmtree(enabled_tweaks_dir, ignore_errors=True)

        # Add files to the enabled tweaks folder
        copytree(src=source_dir, dst=enabled_tweaks_dir, dirs_exist_ok=True)

        self.generate_and_restore(update_label, update_bar)

    def generate_and_restore(self, update_label=lambda x: None, update_bar=lambda y: None):
        # Generate backup
        update_label("Generating backup...")
        backup_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)).joinpath("CowabungaLiteData").joinpath("Backup")
        rmtree(path=backup_dir, ignore_errors=True)
        enabled_tweaks_dir = Path(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)).joinpath("CowabungaLiteData").joinpath("EnabledTweaks")
        backup_created = create_backup(src=enabled_tweaks_dir, dst=backup_dir.joinpath(self.get_current_device_uuid()))
        if not backup_created:
            update_label("Failed to generate backup...")
        
        # Restore backup
        update_label("Restoring backup to device...")
        if self.restore_backup_to_device(backup_dir=backup_dir, update_bar=update_bar):
            update_label("Done!")
        else:
            update_label("Failed.")

    def restore_backup_to_device(self, backup_dir: str, update_bar=lambda x: None) -> bool:
        # restore args: -u [udid] -s Backup restore --system --skip-apps [backup directory]
        ld = create_using_usbmux(serial=self.get_current_device_uuid())
        backup_client = Mobilebackup2Service(lockdown=ld)
        try:
            backup_client.restore(
                backup_directory=backup_dir, progress_callback=update_bar,
                system=True, reboot=True, copy=False, settings=False, remove=False)
        except Exception as e:
            print(traceback.format_exc())
            detailsBox = QMessageBox()
            detailsBox.setIcon(QMessageBox.Critical)
            detailsBox.setWindowTitle("Error!")
            detailsBox.setText(type(e).__name__)
            detailsBox.setDetailedText(str(traceback.format_exc()))
            detailsBox.exec()
            return False
        QMessageBox.information(None, "Success!", "All done! Your device will now restart.\n\nYou should see a black loading screen after entering your passcode - it will disappear after a few seconds.\n\nImportant: If you are presented with a setup, select \"Customize\" > \"Don't transfer apps and data\" and your phone should return to the homescreen as normal.")
        return True
