from PySide6 import QtCore, QtWidgets

from devicemanagement.device_manager import DeviceManager

tweak_tabs = [
    "Home",
    "Explore",
    "Springboard Options",
    "Apply"
]

class MainWindow(QtWidgets.QWidget):
    def __init__(self, device_manager: DeviceManager):
        super().__init__()
        self.device_manager = device_manager

        ### SIDE PANEL

        ## Device Options
        # Create the dropdown and buttons
        self.devices = QtWidgets.QComboBox()
        self.devices.addItem('None')

        self.refresh_btn = QtWidgets.QPushButton('Refresh')

        device_layout = QtWidgets.QHBoxLayout()
        device_layout.addWidget(self.devices)
        device_layout.addWidget(self.refresh_btn)
        layout_widget = QtWidgets.QWidget()
        layout_widget.setLayout(device_layout)

        # Connect the actions
        self.refresh_btn.clicked.connect(self.refresh_devices)
        self.devices.currentIndexChanged.connect(self.change_selected_device)

        ## Tabs
        menu_bar = QtWidgets.QListWidget()
        for tab in tweak_tabs:
            item = QtWidgets.QListWidgetItem(tab)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            menu_bar.addItem(item)
        side_bar_layout = QtWidgets.QVBoxLayout()
        side_bar_layout.addWidget(layout_widget)
        side_bar_layout.addWidget(menu_bar)
        side_bar_widget = QtWidgets.QWidget()
        side_bar_widget.setLayout(side_bar_layout)

        ### CONTENT
        text_widget = QtWidgets.QLabel("Placeholder")
        content_layout = QtWidgets.QVBoxLayout()
        content_layout.addWidget(text_widget)
        main_widget = QtWidgets.QWidget()
        main_widget.setLayout(content_layout)

        ### MAIN LAYOUT
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(side_bar_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

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