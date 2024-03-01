from PySide6 import QtCore, QtWidgets
from enum import Enum

from ui_mainwindow import Ui_CowabungaLite

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

    ## DEVICE BAR FUNCTIONS
    @QtCore.Slot()
    def refresh_devices(self):
        self.device_manager.get_devices()
        self.ui.devicePicker.clear()
        if len(self.device_manager.devices) == 0:
            self.ui.devicePicker.addItem('None')
        else:
            for device in self.device_manager.devices:
                self.ui.devicePicker.addItem(device.name)

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