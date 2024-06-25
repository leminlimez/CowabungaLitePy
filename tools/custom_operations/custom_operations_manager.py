import os
import plistlib
import shutil
from pathlib import Path

from PySide6.QtCore import QStandardPaths, QDir, QFileInfo, QStandardPaths

from tools.custom_operations.operation_objects import AdvancedObject
from utils.icon_utils import unzip

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

    def import_operation(self, selected_file: str) -> bool:
        if selected_file:
            fileInfo = QFileInfo(selected_file)
            regex = "\\.(cowperation)$"
            zipName = fileInfo.fileName().replace(regex, "")

            cblDataPath = os.path.join(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation), "CowabungaLiteData")
            operationsDir = os.path.join(cblDataPath, "Operations")
            tempDirPath = os.path.join(cblDataPath, "temp")
            operationDirPath = os.path.join(tempDirPath, zipName)
            operationDir = QDir(operationDirPath)

            if operationDir.exists():
                operationDir.removeRecursively()
            else:
                if not operationDir.mkpath("."):
                    print("Failed to create the directory:", operationDir)
                else:
                    unzip(selected_file, operationDirPath)
                    for child in os.listdir(operationDirPath):
                        op_path = os.path.join(str(operationDirPath), child)
                        if os.path.isdir(op_path) and not child.startswith('.'):
                            shutil.move(op_path, os.path.join(operationsDir, child))
                    shutil.rmtree(tempDirPath)
                    self.reload_operations()
                    return True
        return False