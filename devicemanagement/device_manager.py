import os
from pathlib import Path
from shutil import copytree

from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux
import pymobiledevice3.services.diagnostics as diagnostics

from devicemanagement.constants import Device
from devicemanagement.data_singleton import DataSingleton

class DeviceManager:
    ## Class Functions
    def __init__(self):
        self.devices: list[Device] = []
        self.data_singleton = DataSingleton()
    
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
                self.devices.append(dev)
            except:
                print(f"ERROR with lockdown device with UUID {device.serial}")
        
        if len(connected_devices) > 0:
            self.data_singleton.current_device = connected_devices[0]
        else:
            self.data_singleton.current_device = None

    def setup_workspace(self, uuid: str):
        # create the workspace for the uuid
        path: Path = Path(os.getcwd()).joinpath("CowabungaLiteData").joinpath("Workspace").joinpath(uuid)
        path.mkdir(parents=True, exist_ok=True)
        files_path: Path = Path(os.getcwd()).joinpath("file_folders").joinpath("files")
        copytree(src=files_path, dst=path)
        self.data_singleton.current_workspace = path