import os
import plistlib
from pathlib import Path

from PySide6.QtCore import QStandardPaths, QCoreApplication, QDir

from tools.custom_operations.operation_objects import AdvancedObject

class CustomOperationsManager:
    def __init__(self):
        self.operations: list = [] # list of custom operations

    def reload_operations(self):
        self.operations.clear()
        app_data_dir = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        path = Path(app_data_dir).joinpath("CowabungaLiteData").joinpath("Operations")
        path.mkdir(parents=True, exist_ok=True)
        for op in os.listdir(str(path)):
            op_path = os.path.join(str(path), op)
            if os.path.isdir(op_path) and not op.startswith('.'):
                # get the operation data
                try:
                    with open(os.path.join(op_path, "Info.plist"), 'rb') as in_fp:
                        plist = plistlib.load(in_fp)
                    author: str = plist["Author"] if "Author" in plist else ""
                    version: str = plist["Version"] if "Version" in plist else "1.0"
                    locked: bool = plist["Locked"] if "Locked" in plist else False
                    icon: str = None
                    iconPath = os.path.join(op_path, "Icon.png")
                    if os.path.isfile(iconPath):
                        icon = iconPath
                    # create the operation and add it to the list
                    new_op = AdvancedObject(name=op, filePath=op_path, author=author, version=version, icon=icon, locked=locked)
                    self.operations.append(new_op)
                except:
                    pass

    def delete_operation(self, operation: AdvancedObject):
        if operation in self.operations:
            self.operations.remove(operation)
            QDir(operation.filePath).removeRecursively()