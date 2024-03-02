from PySide6 import QtCore, QtWidgets
from enum import Enum

from ui_mainwindow import Ui_CowabungaLite

from devicemanagement.constants import Version
from devicemanagement.device_manager import DeviceManager

class Page(Enum):
    Home = 0
    Explore = 1
    LocSim = 2
    Themes = 3
    StatusBar = 4
    ControlCenter = 5
    SpringboardOptions = 6
    InternalOptions = 7
    SetupOptions = 8
    Apply = 9

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, device_manager: DeviceManager):
        super(MainWindow, self).__init__()
        self.device_manager = device_manager
        self.ui = Ui_CowabungaLite()
        self.ui.setupUi(self)

        ## DEVICE BAR
        self.refresh_devices()

        self.ui.refreshBtn.clicked.connect(self.refresh_devices)
        self.ui.devicePicker.currentIndexChanged.connect(self.change_selected_device)

        ## SIDE BAR ACTIONS
        self.ui.homePageBtn.clicked.connect(self.on_homePageBtn_clicked)
        self.ui.explorePageBtn.clicked.connect(self.on_explorePageBtn_clicked)
        self.ui.locSimPageBtn.clicked.connect(self.on_locSimPageBtn_clicked)
        self.ui.themesPageBtn.clicked.connect(self.on_themesPageBtn_clicked)
        self.ui.statusBarPageBtn.clicked.connect(self.on_statusBarPageBtn_clicked)
        self.ui.controlCenterPageBtn.clicked.connect(self.on_controlCenterPageBtn_clicked)
        self.ui.springboardOptionsPageBtn.clicked.connect(self.on_springboardOptionsPageBtn_clicked)
        self.ui.internalOptionsPageBtn.clicked.connect(self.on_internalOptionsPageBtn_clicked)
        self.ui.setupOptionsPageBtn.clicked.connect(self.on_setupOptionsPageBtn_clicked)
        self.ui.applyPageBtn.clicked.connect(self.on_applyPageBtn_clicked)

    ## GENERAL INTERFACE FUNCTIONS
    def updateInterfaceForNewDevice(self):
        # update the home page
        self.updatePhoneInfo()

        if self.device_manager.data_singleton.device_available:
            # TODO: Load LocSim
            # TODO: Load Pages
            pass
        
        # TODO: update enabled tweaks

    ## DEVICE BAR FUNCTIONS
    @QtCore.Slot()
    def refresh_devices(self):
        # get the devices
        self.device_manager.get_devices()
        # clear the picker
        self.ui.devicePicker.clear()
        if len(self.device_manager.devices) == 0:
            self.ui.devicePicker.setEnabled(False)
            self.ui.devicePicker.addItem('None')
            self.ui.pages.setCurrentIndex(Page.Home.value)
            self.ui.homePageBtn.setChecked(True)

            # hide all pages
            self.ui.locSimPageBtn.hide()
            self.ui.sidebarDiv1.hide()
            self.ui.themesPageBtn.hide()
            self.ui.statusBarPageBtn.hide()
            self.ui.controlCenterPageBtn.hide()
            self.ui.springboardOptionsPageBtn.hide()
            self.ui.internalOptionsPageBtn.hide()
            self.ui.setupOptionsPageBtn.hide()
            self.ui.sidebarDiv2.hide()
            self.ui.applyPageBtn.hide()
        else:
            self.ui.devicePicker.setEnabled(True)
            # populate the ComboBox with device names
            for device in self.device_manager.devices:
                self.ui.devicePicker.addItem(device.name)
            
            # show all pages
            self.ui.locSimPageBtn.show()
            self.ui.sidebarDiv1.show()
            self.ui.themesPageBtn.show()
            self.ui.statusBarPageBtn.show()
            self.ui.controlCenterPageBtn.show()
            self.ui.springboardOptionsPageBtn.show()
            self.ui.internalOptionsPageBtn.show()
            self.ui.setupOptionsPageBtn.show()
            self.ui.sidebarDiv2.show()
            self.ui.applyPageBtn.show()
        
        # update the selected device
        self.ui.devicePicker.setCurrentIndex(self.device_manager.current_device_index)

        # update the interface
        self.updateInterfaceForNewDevice()

    def change_selected_device(self, index):
        if len(self.device_manager.devices) > 0:
            self.device_manager.set_current_device(index=index)
        else:
            self.device_manager.set_current_device(index=None)
    

    ## SIDE BAR FUNCTIONS
    def on_homePageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Home.value)

    def on_explorePageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Explore.value)
        # TODO: load explore page

    def on_locSimPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.LocSim.value)
    
    def on_themesPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Themes.value)

    def on_statusBarPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.StatusBar.value)
    
    def on_controlCenterPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.ControlCenter.value)

    def on_springboardOptionsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.SpringboardOptions.value)

    def on_internalOptionsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.InternalOptions.value)

    def on_setupOptionsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.SetupOptions.value)

    def on_applyPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.Apply.value)
    

    ## HOME PAGE
    def updatePhoneInfo(self):
        # name label
        self.ui.phoneNameLbl.setText(self.device_manager.get_current_device_name())
        # version label
        ver = self.device_manager.get_current_device_version()
        if ver != "":
            parsed_ver: Version = Version(ver)
            support_str: str = "<span style=\"color: #32d74b;\">Supported!</span></a>"
            if parsed_ver > DeviceManager.last_tested_version:
                support_str = "<span style=\"color: #ffff00;\">Supported, YMMV.</span></a>"
            elif parsed_ver < DeviceManager.min_version:
                support_str = "<span style=\"color: #ff0000;\">Not Supported.</span></a>"
            self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white;\" href=\"#\">iOS {ver} {support_str}")
        else:
            self.ui.phoneVersionLbl.setText("Please connect a device.")