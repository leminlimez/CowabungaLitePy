from PySide6 import QtCore, QtWidgets
from enum import Enum

from pymobiledevice3.lockdown import create_using_usbmux

from ui_mainwindow import Ui_CowabungaLite

from devicemanagement.constants import Version
from devicemanagement.device_manager import DeviceManager

from tools.locsim import mount_dev_disk

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
        self.show_uuid = False
        self.location_loading = False

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

        ## HOME PAGE ACTIONS
        self.ui.phoneVersionLbl.linkActivated.connect(self.toggle_version_label)

        ## LOC SIM PAGE ACTIONS
        self.ui.loadLocSimBtn.clicked.connect(self.on_loadLocSimBtn_clicked)


    ## GENERAL INTERFACE FUNCTIONS
    def updateInterfaceForNewDevice(self):
        # update the home page
        self.updatePhoneInfo()

        if self.device_manager.data_singleton.device_available:
            # Load LocSim
            self.ui.locSimCnt.hide()
            self.ui.loadLocSimBtn.show()
            self.ui.loadLocSimBtn.setEnabled(True)
            self.ui.loadLocSimBtn.setText("Start Location Simulation")

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
        self.ui.devicePicker.setCurrentIndex(0)

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
        self.show_uuid = False
        if ver != "":
            self.show_version_text(version=ver)
        else:
            self.ui.phoneVersionLbl.setText("Please connect a device.")

    def toggle_version_label(self):
        if self.show_uuid:
            self.show_uuid = False
            ver = self.device_manager.get_current_device_version()
            if ver != "":
                self.show_version_text(version=ver)
        else:
            self.show_uuid = True
            uuid = self.device_manager.get_current_device_uuid()
            if uuid != "":
                self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white\" href=\"#\">{uuid}</a>")

    def show_version_text(self, version: str):
        parsed_ver: Version = Version(version)
        support_str: str = "<span style=\"color: #32d74b;\">Supported!</span></a>"
        if parsed_ver > DeviceManager.last_tested_version:
            support_str = "<span style=\"color: #ffff00;\">Supported, YMMV.</span></a>"
        elif parsed_ver < DeviceManager.min_version:
            support_str = "<span style=\"color: #ff0000;\">Not Supported.</span></a>"
        self.ui.phoneVersionLbl.setText(f"<a style=\"text-decoration:none; color: white;\" href=\"#\">iOS {version} {support_str}")

    
    ## LOC SIM PAGE
    def on_loadLocSimBtn_clicked(self):
        if self.device_manager.data_singleton.current_device != None and self.location_loading != True:
            self.location_loading = True
            self.ui.loadLocSimBtn.setText("Loading...")
            # mount the disk
            device = self.device_manager.data_singleton.current_device
            ld = create_using_usbmux(serial=device.uuid)
            result: str = mount_dev_disk(device=device, ld=ld)
            if result == "Success" or result == "DeveloperDiskImage already mounted":
                self.ui.loadLocSimBtn.hide()
                self.ui.locSimCnt.show()
            else:
                self.ui.loadLocSimBtn.setText(result)
            self.location_loading = False