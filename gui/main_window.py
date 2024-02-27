from PySide6 import QtCore, QtWidgets

from devicemanagement.device_manager import DeviceManager

class MainWindow(QtWidgets.QWidget):
    def __init__(self, device_manager: DeviceManager):
        super().__init__()
        self.device_manager = device_manager

        # Create the dropdown and buttons
        self.devices = QtWidgets.QComboBox()
        self.devices.addItem('None')

        self.refresh_btn = QtWidgets.QPushButton('Refresh')

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.devices)
        self.layout.addWidget(self.refresh_btn)

        # Connect the actions
        self.refresh_btn.clicked.connect(self.refresh_devices)
        self.devices.currentIndexChanged.connect(self.change_selected_device)

    @QtCore.Slot()
    def refresh_devices(self):
        self.device_manager.get_devices()
        self.devices.clear()
        if len(self.device_manager.devices) == 0:
            self.devices.addItem('None')
        else:
            for device in self.device_manager.devices:
                self.devices.addItem(device.name)

    def change_selected_device(self, index):
        if len(self.device_manager.devices) > 0:
            self.device_manager.set_current_device(index=index)
        else:
            self.device_manager.set_current_device(index=None)