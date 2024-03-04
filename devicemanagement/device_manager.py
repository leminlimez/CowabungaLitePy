import os
from pathlib import Path
from shutil import copytree

from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux
import pymobiledevice3.services.diagnostics as diagnostics

from devicemanagement.constants import Device, Version
from devicemanagement.data_singleton import DataSingleton

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
        # TODO: maybe try get_home_folder() from pymobiledevice3.common?
        path: Path = Path(os.path.expanduser("~/Documents")).joinpath("CowabungaLiteData").joinpath("Workspace").joinpath(uuid)
        path.mkdir(parents=True, exist_ok=True)
        # TODO: Copy subfolders of files into path if not there
        #files_path: Path = Path(os.getcwd()).joinpath("file_folders").joinpath("files")
        #copytree(src=files_path, dst=path)
        self.data_singleton.current_workspace = path