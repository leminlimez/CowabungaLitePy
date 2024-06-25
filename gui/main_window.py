from PySide6 import QtCore, QtWidgets, QtGui
from enum import Enum
from pathlib import Path
import webbrowser
import os

from pymobiledevice3.lockdown import create_using_usbmux

from ui_mainwindow import Ui_CowabungaLite

from devicemanagement.constants import Version, Tweak, FileLocation
from devicemanagement.device_manager import DeviceManager

from tools.locsim import mount_dev_disk, LocSimManager
from tools.status_bar.status_manager import StatusSetter

from tools.custom_operations.custom_operations_manager import CustomOperationsManager

from utils.plist_manager import get_plist_value, set_plist_value, delete_plist_key
from utils.icon_utils import createRoundedPixmap

class Page(Enum):
    Home = 0
    Explore = 1
    LocSim = 2
    CustomOperations = 5
    Themes = 3
    StatusBar = 4
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
        self.locsim_manager: LocSimManager = None
        
        # Initialize the custom operations
        self.operations_manager = CustomOperationsManager()

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
        self.ui.customOperationsPageBtn.clicked.connect(self.on_customOperationsPageBtn_clicked)
        self.ui.springboardOptionsPageBtn.clicked.connect(self.on_springboardOptionsPageBtn_clicked)
        self.ui.internalOptionsPageBtn.clicked.connect(self.on_internalOptionsPageBtn_clicked)
        self.ui.setupOptionsPageBtn.clicked.connect(self.on_setupOptionsPageBtn_clicked)
        self.ui.applyPageBtn.clicked.connect(self.on_applyPageBtn_clicked)

        ## HOME PAGE ACTIONS
        self.ui.phoneVersionLbl.linkActivated.connect(self.toggle_version_label)

        ## HOME PAGE LINKS
        self.ui.bigMilkBtn.clicked.connect(self.on_bigMilkBtn_clicked)

        self.ui.leminGitHubBtn.clicked.connect(self.on_leminGitHubBtn_clicked)
        self.ui.leminTwitterBtn.clicked.connect(self.on_leminTwitterBtn_clicked)
        self.ui.leminKoFiBtn.clicked.connect(self.on_leminKoFiBtn_clicked)

        self.ui.avangelistaGitHubBtn.clicked.connect(self.on_avangelistaGitHubBtn_clicked)
        self.ui.avangelistaTwitterBtn.clicked.connect(self.on_avangelistaTwitterBtn_clicked)
        self.ui.avangelistaKoFiBtn.clicked.connect(self.on_avangelistaKoFiBtn_clicked)
        
        self.ui.iTechBtn.clicked.connect(self.on_iTechBtn_clicked)
        self.ui.libiBtn.clicked.connect(self.on_libiBtn_clicked)
        self.ui.qtBtn.clicked.connect(self.on_qtBtn_clicked)
        self.ui.discordBtn.clicked.connect(self.on_discordBtn_clicked)

        ## LOC SIM PAGE ACTIONS
        self.ui.loadLocSimBtn.clicked.connect(self.on_loadLocSimBtn_clicked)
        self.ui.setLocationBtn.clicked.connect(self.on_setLocationBtn_clicked)
        self.ui.resetLocationBtn.clicked.connect(self.on_resetLocationBtn_clicked)

        ## SPRINGBOARD OPTIONS PAGE ACTIONS
        self.ui.springboardOptionsEnabledChk.toggled.connect(self.on_springboardOptionsEnabledChk_toggled)
        self.ui.UIAnimSpeedSld.sliderMoved.connect(self.on_UIAnimSpeedSld_sliderMoved)
        self.ui.footnoteTxt.textEdited.connect(self.on_footnoteTxt_textEdited)
        self.ui.disableLockRespringChk.toggled.connect(self.on_disableLockRespringChk_clicked)
        self.ui.disableDimmingChk.toggled.connect(self.on_disableDimmingChk_clicked)
        self.ui.disableBatteryAlertsChk.toggled.connect(self.on_disableBatteryAlertsChk_clicked)
        self.ui.disableCrumbChk.toggled.connect(self.on_disableCrumbChk_clicked)
        self.ui.enableSupervisionTextChk.toggled.connect(self.on_enableSupervisionTextChk_clicked)
        self.ui.enableWiFiDebuggerChk.toggled.connect(self.on_enableWiFiDebuggerChk_clicked)
        self.ui.enableShutdownSoundChk.toggled.connect(self.on_enableShutdownSoundChk_clicked)
        self.ui.allowAirDropEveryoneChk.toggled.connect(self.on_allowAirDropEveryoneChk_clicked)

        ## INTERNAL OPTIONS PAGE ACTIONS
        self.ui.internalOptionsEnabledChk.toggled.connect(self.on_internalOptionsEnabledChk_toggled)
        self.ui.buildVersionChk.toggled.connect(self.on_buildVersionChk_clicked)
        self.ui.RTLChk.toggled.connect(self.on_RTLChk_clicked)
        self.ui.metalHUDChk.toggled.connect(self.on_metalHUDChk_clicked)
        self.ui.accessoryChk.toggled.connect(self.on_accessoryChk_clicked)
        self.ui.iMessageChk.toggled.connect(self.on_iMessageChk_clicked)
        self.ui.IDSChk.toggled.connect(self.on_IDSChk_clicked)
        self.ui.VCChk.toggled.connect(self.on_VCChk_clicked)
        self.ui.appStoreChk.toggled.connect(self.on_appStoreChk_clicked)
        self.ui.notesChk.toggled.connect(self.on_notesChk_clicked)
        self.ui.showTouchesChk.toggled.connect(self.on_showTouchesChk_clicked)
        self.ui.hideRespringChk.toggled.connect(self.on_hideRespringChk_clicked)
        self.ui.enableWakeVibrateChk.toggled.connect(self.on_enableWakeVibrateChk_clicked)
        self.ui.pasteSoundChk.toggled.connect(self.on_pasteSoundChk_clicked)
        self.ui.notifyPastesChk.toggled.connect(self.on_notifyPastesChk_clicked)

        ## SETUP OPTIONS PAGE
        self.ui.setupOptionsEnabledChk.toggled.connect(self.on_setupOptionsEnabledChk_toggled)
        self.ui.skipSetupChk.toggled.connect(self.on_skipSetupChk_clicked)
        self.ui.enableSupervisionChk.toggled.connect(self.on_enableSupervisionChk_clicked)
        self.ui.organizationNameTxt.textEdited.connect(self.on_organizationNameTxt_textEdited)

        ## APPLY PAGE ACTIONS
        self.ui.applyTweaksBtn.clicked.connect(self.on_applyPageBtn_clicked)
        self.ui.removeTweaksBtn.clicked.connect(self.on_removeTweaksBtn_clicked)
        self.ui.deepCleanBtn.clicked.connect(self.on_deepCleanBtn_clicked)

        ## STATUS BAR PAGE ACTIONS
        self.ui.statusBarEnabledChk.toggled.connect(self.on_statusBarEnabledChk_toggled)
        # PRIMARY CARRIER
        self.ui.pDefaultRdo.clicked.connect(self.on_pDefaultRdo_clicked)
        self.ui.pShowRdo.clicked.connect(self.on_pShowRdo_clicked)
        self.ui.pHideRdo.clicked.connect(self.on_pHideRdo_clicked)
        self.ui.pCarrierChk.toggled.connect(self.on_pCarrierChk_clicked)
        self.ui.pCarrierTxt.textEdited.connect(self.on_pCarrierTxt_textEdited)
        self.ui.pBadgeChk.toggled.connect(self.on_pBadgeChk_clicked)
        self.ui.pBadgeTxt.textEdited.connect(self.on_pBadgeTxt_textEdited)
        self.ui.pTypeChk.toggled.connect(self.on_pTypeChk_clicked)
        self.ui.pTypeDrp.activated.connect(self.on_pTypeDrp_activated)
        self.ui.pStrengthChk.toggled.connect(self.on_pStrengthChk_clicked)
        self.ui.pStrengthSld.sliderMoved.connect(self.on_pStrengthSld_sliderMoved)
        # SECONDARY CARRIER
        self.ui.sDefaultRdo.clicked.connect(self.on_sDefaultRdo_clicked)
        self.ui.sShowRdo.clicked.connect(self.on_sShowRdo_clicked)
        self.ui.sHideRdo.clicked.connect(self.on_sHideRdo_clicked)
        self.ui.sCarrierChk.toggled.connect(self.on_sCarrierChk_clicked)
        self.ui.sCarrierTxt.textEdited.connect(self.on_sCarrierTxt_textEdited)
        self.ui.sBadgeChk.toggled.connect(self.on_sBadgeChk_clicked)
        self.ui.sBadgeTxt.textEdited.connect(self.on_sBadgeTxt_textEdited)
        self.ui.sTypeChk.toggled.connect(self.on_sTypeChk_clicked)
        self.ui.sTypeDrp.activated.connect(self.on_sTypeDrp_activated)
        self.ui.sStrengthChk.toggled.connect(self.on_sStrengthChk_clicked)
        self.ui.sStrengthSld.sliderMoved.connect(self.on_sStrengthSld_sliderMoved)
        # MISC TEXT INPUTS
        self.ui.timeChk.clicked.connect(self.on_timeChk_clicked)
        self.ui.timeTxt.textEdited.connect(self.on_timeTxt_textEdited)
        self.ui.breadcrumbChk.clicked.connect(self.on_breadcrumbChk_clicked)
        self.ui.breadcrumbTxt.textEdited.connect(self.on_breadcrumbTxt_textEdited)
        self.ui.batteryDetailChk.clicked.connect(self.on_batteryDetailChk_clicked)
        self.ui.batteryDetailTxt.textEdited.connect(self.on_batteryDetailTxt_textEdited)
        # MISC SLIDER INPUTS
        self.ui.batteryCapacityChk.clicked.connect(self.on_batteryCapacityChk_clicked)
        self.ui.batteryCapacitySld.sliderMoved.connect(self.on_batteryCapacitySld_sliderMoved)
        self.ui.wifiStrengthChk.clicked.connect(self.on_wifiStrengthChk_clicked)
        self.ui.wifiStrengthSld.sliderMoved.connect(self.on_wifiStrengthSld_sliderMoved)
        # RAW SIGNAL STRENGTH INPUTS
        self.ui.numericWifiChk.clicked.connect(self.on_numericWifiChk_clicked)
        self.ui.numericCellChk.clicked.connect(self.on_numericCellChk_clicked)
        # HIDE OPTION INPUTS
        self.ui.hideDNDChk.clicked.connect(self.on_hideDNDChk_clicked)
        self.ui.hideAirplaneChk.clicked.connect(self.on_hideAirplaneChk_clicked)
        self.ui.hideWifiChk.clicked.connect(self.on_hideWifiChk_clicked)
        self.ui.hideBatteryChk.clicked.connect(self.on_hideBatteryChk_clicked)
        self.ui.hideBluetoothChk.clicked.connect(self.on_hideBatteryChk_clicked)
        self.ui.hideAlarmChk.clicked.connect(self.on_hideAlarmChk_clicked)
        self.ui.hideLocationChk.clicked.connect(self.on_hideLocationChk_clicked)
        self.ui.hideRotationChk.clicked.connect(self.on_hideRotationChk_clicked)
        self.ui.hideAirPlayChk.clicked.connect(self.on_hideAirPlayChk_clicked)
        self.ui.hideCarPlayChk.clicked.connect(self.on_hideCarPlayChk_clicked)
        self.ui.hideVPNChk.clicked.connect(self.on_hideVPNChk_clicked)


    ## GENERAL INTERFACE FUNCTIONS
    def updateInterfaceForNewDevice(self):
        # update the home page
        self.updatePhoneInfo()
        self.load_custom_operations_page()

        if self.device_manager.data_singleton.device_available:
            # Load LocSim
            self.ui.locSimCnt.hide()
            self.ui.loadLocSimBtn.show()
            self.ui.loadLocSimBtn.setEnabled(True)
            self.ui.loadLocSimBtn.setText("Start Location Simulation")
            self.location_loading = False

            # TODO: Load Pages
            self.load_status_bar()
            self.load_springboard_options()
            self.load_internal_options()
            self.load_setup_options()
        
        # TODO: update enabled tweaks
        self.update_enabled_tweaks()

    def update_enabled_tweaks(self):
        tweaks = self.device_manager.data_singleton.enabled_tweaks
        label_txt = ""
        if len(tweaks) == 0:
            label_txt = "None"
            self.ui.applyTweaksBtn.setDisabled(True)
        else:
            first_tweak: bool = True
            for tweak in tweaks:
                if not first_tweak:
                    label_txt += ", "
                else:
                    first_tweak = False
                label_txt += tweak.value
            self.ui.applyTweaksBtn.setDisabled(False)
            
        self.ui.enabledTweaksLbl.setText(label_txt)

        #self.ui.themesEnabledChk.setChecked()
        self.ui.statusBarEnabledChk.setChecked(Tweak.StatusBar in tweaks)
        self.ui.springboardOptionsEnabledChk.setChecked(Tweak.SpringboardOptions in tweaks)
        self.ui.internalOptionsEnabledChk.setChecked(Tweak.InternalOptions in tweaks)
        self.ui.setupOptionsEnabledChk.setChecked(Tweak.SkipSetup in tweaks)

    def set_key(self, key: str, checked: bool, loc: FileLocation):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, loc.value)
        if checked:
            set_plist_value(location, key, checked)
        else:
            delete_plist_key(location, key)


    ## DEVICE BAR FUNCTIONS
    @QtCore.Slot()
    def refresh_devices(self):
        # get the devices
        self.device_manager.get_devices()
        # clear the picker
        self.ui.devicePicker.clear()
        self.ui.restoreProgressBar.hide()
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
    
    def on_customOperationsPageBtn_clicked(self):
        self.ui.pages.setCurrentIndex(Page.CustomOperations.value)

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

    ## HOME PAGE LINKS
    def on_bigMilkBtn_clicked(self):
        webbrowser.open_new_tab("https://cowabun.ga")

    def on_leminGitHubBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/leminlimez")
    def on_leminTwitterBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/LeminLimez")
    def on_leminKoFiBtn_clicked(self):
        webbrowser.open_new_tab("https://ko-fi.com/leminlimez")

    def on_avangelistaGitHubBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/Avangelista")
    def on_avangelistaTwitterBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/AvangelistaDev")
    def on_avangelistaKoFiBtn_clicked(self):
        webbrowser.open_new_tab("https://ko-fi.com/avangelista")

    def on_iTechBtn_clicked(self):
        webbrowser.open_new_tab("https://twitter.com/iTechExpert21")
    def on_libiBtn_clicked(self):
        webbrowser.open_new_tab("https://github.com/doronz88/pymobiledevice3")
    def on_qtBtn_clicked(self):
        webbrowser.open_new_tab("https://www.qt.io/product/development-tools")

    def on_discordBtn_clicked(self):
        webbrowser.open_new_tab("https://discord.gg/MN8JgqSAqT")


    ## CUSTOM OPERATIONS PAGE
    def delete_operation(self, operation):
        self.operations_manager.delete_operation(operation)
        self.load_custom_operations_page()

    def load_custom_operations_page(self):
        self.operations_manager.reload_operations()

        # Clear the layout
        layout = self.ui.operationsCnt.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                widget = child.widget()
                if widget:
                    widget.deleteLater()
                del child
            del layout

        # Clear the widget contents
        for child in self.ui.operationsCnt.children():
            child.deleteLater()

        # Create a grid layout
        mainLayout = QtWidgets.QGridLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        if len(self.operations_manager.operations) == 0:
            layout = QtWidgets.QVBoxLayout(self.ui.operationsCnt)
            label = QtWidgets.QLabel("No operations found. Import one or create a new one.")
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)
            self.ui.operationsCnt.setLayout(layout)
            return
        
        # Iterate through the operations
        for operation in self.operations_manager.operations:
            widget = QtWidgets.QWidget()
            widget.setFixedSize(300, 140)
            widget.setStyleSheet("QWidget { background: none; border: 1px solid #3b3b3b; border-radius: 8px; }")

            # create the icon
            icon = QtGui.QPixmap(operation.icon) if operation.icon != None else QtGui.QPixmap(":/missing.png")
            iconBtn = QtWidgets.QToolButton(widget)
            iconBtn.setIcon(QtGui.QIcon(createRoundedPixmap(icon, 0.25)))
            iconBtn.setIconSize(QtCore.QSize(45, 45))
            iconBtn.setStyleSheet("QToolButton { margin-left: 8px; min-height: 0px; background: none; padding: 0px; border: none; }")

            # create the name and author
            nameContainer = QtWidgets.QWidget()
            nameContainer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            nameContainer.setFixedHeight(60)
            nameContainer.setStyleSheet("QWidget { border: none; }")

            nameLabel = QtWidgets.QLabel(operation.name)
            nameLabel.setFixedHeight(20)
            nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            nameLabel.setStyleSheet("QLabel { border: none; }")
            authorLabel = QtWidgets.QLabel(operation.author if operation.author != "" else "No Author")
            authorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            authorLabel.setStyleSheet("QLabel {	font-size: 10px; border: none;}")

            nameLayout = QtWidgets.QVBoxLayout(nameContainer)
            nameLayout.addWidget(nameLabel)
            nameLayout.addWidget(authorLabel)
            nameContainer.setLayout(nameLayout)

            infoLayout = QtWidgets.QHBoxLayout()
            infoLayout.addWidget(iconBtn)
            infoLayout.addWidget(nameContainer)

            # create the buttons
            # edit button
            editBtn = QtWidgets.QToolButton(widget)
            editBtn.setText("Edit")
            editBtn.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            editBtn.setStyleSheet("QToolButton { margin-left: 8px; background-color: #3b3b3b; border: none; }\nQToolButton:pressed { background-color: #535353; color: #FFFFFF; }")
            #editBtn.clicked.connect(lambda _, dir=operation.filePath: DeviceManager.getInstance().applyTheme(dir))
            # delete button
            delBtn = QtWidgets.QToolButton(widget)
            delBtn.setIcon(QtGui.QIcon(":/icon/trash.svg"))
            delBtn.setStyleSheet("QToolButton { margin-right: 8px; background-color: #3b3b3b; border: none; }\nQToolButton:pressed { background-color: #535353; color: #FFFFFF; }")
            delBtn.clicked.connect(lambda _, op=operation: self.delete_operation(op))
            btnLayout = QtWidgets.QHBoxLayout()
            btnLayout.addWidget(editBtn)
            btnLayout.addWidget(delBtn)

            # main layout
            layout = QtWidgets.QVBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 9)
            layout.addLayout(infoLayout)
            # modify toggle
            if self.device_manager.data_singleton.device_available:
                modifyToggle = QtWidgets.QCheckBox("Enabled")
                modifyToggle.setChecked(operation.enabled)
                modifyToggle.setStyleSheet("QCheckBox { margin-left: 8px; border: none; }")
                modifyToggle.toggled.connect(operation.set_enabled)
                layout.addWidget(modifyToggle)
            layout.addLayout(btnLayout)
            widget.setLayout(layout)

            # Add the widget to the mainLayout
            mainLayout.addWidget(widget)

        # Create a QWidget to act as the container for the scroll area
        scrollWidget = QtWidgets.QWidget()

        # Set the main layout (containing all the widgets) on the scroll widget
        scrollWidget.setLayout(mainLayout)

        # Create a QScrollArea to hold the content widget (scrollWidget)
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)  # Allow the content widget to resize within the scroll area
        scrollArea.setFrameStyle(QtWidgets.QScrollArea.NoFrame)  # Remove the outline from the scroll area

        # Set the scrollWidget as the content widget of the scroll area
        scrollArea.setWidget(scrollWidget)

        # Set the size policy of the scroll area to expand in both directions
        scrollArea.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Set the scroll area as the central widget of the main window
        scrollLayout = QtWidgets.QVBoxLayout()
        scrollLayout.setContentsMargins(0, 0, 0, 0)
        scrollLayout.addWidget(scrollArea)
        self.ui.operationsCnt.setLayout(scrollLayout)


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
                self.locsim_manager = LocSimManager(lockdown=ld)
                self.ui.locSimCnt.show()
            else:
                self.ui.loadLocSimBtn.setText(result)
            self.location_loading = False
    
    def on_setLocationBtn_clicked(self):
        if self.locsim_manager != None:
            self.locsim_manager.set(lat=int(self.ui.latitudeTxt.text()), long=int(self.ui.longitudeTxt.text()))

    def on_resetLocationBtn_clicked(self):
        if self.locsim_manager != None:
            self.locsim_manager.reset()


    ## STATUS BAR PAGE
    def on_statusBarEnabledChk_toggled(self, checked: bool):
        self.ui.statusBarPageContent.setDisabled(not checked)
        self.device_manager.data_singleton.set_tweak_enabled(tweak=Tweak.StatusBar, enabled=checked)
        self.update_enabled_tweaks()

    # PRIMARY CARRIER
    def on_pDefaultRdo_clicked(self):
        if self.status_manager != None:
            self.status_manager.unset_cellular_service()
    def on_pShowRdo_clicked(self):
        if self.status_manager != None:
            self.status_manager.set_cellular_service(True)
    def on_pHideRdo_clicked(self):
        if self.status_manager != None:
            self.status_manager.set_cellular_service(False)
    def on_pCarrierChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_carrier_override(str(self.ui.pCarrierTxt.text()))
            else:
                self.status_manager.unset_carrier_override()
    def on_pCarrierTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.pCarrierChk.isChecked():
                self.status_manager.set_carrier_override(text)
    def on_pBadgeChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_primary_service_badge(str(self.ui.pBadgeTxt.text()))
            else:
                self.status_manager.unset_primary_service_badge()
    def on_pBadgeTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.pBadgeChk.isChecked():
                self.status_manager.set_primary_service_badge(text)
    def on_pTypeChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_data_network_type(self.ui.pTypeDrp.currentIndex())
            else:
                self.status_manager.unset_data_network_type()
    def on_pTypeDrp_activated(self, index: int):
        if self.status_manager != None:
            if self.ui.pTypeChk.isChecked():
                self.status_manager.set_data_network_type(self.ui.pTypeDrp.currentIndex())
    def on_pStrengthChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_gsm_signal_strength_bars(self.ui.pStrengthSld.value())
            else:
                self.status_manager.unset_gsm_signal_strength_bars()
    def on_pStrengthSld_sliderMoved(self, pos: int):
        self.ui.pStrengthLbl.setText(str(pos) + (" Bar" if pos == 1 else " Bars"))
        if self.status_manager != None:
            if self.ui.pStrengthChk.isChecked():
                self.status_manager.set_gsm_signal_strength_bars(pos)

    # SECONDARY CARRIER
    def on_sDefaultRdo_clicked(self):
        if self.status_manager != None:
            self.status_manager.unset_secondary_cellular_service()
    def on_sShowRdo_clicked(self):
        if self.status_manager != None:
            self.status_manager.set_secondary_cellular_service(True)
    def on_sHideRdo_clicked(self):
        if self.status_manager != None:
            self.status_manager.set_secondary_cellular_service(False)
    def on_sCarrierChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_secondary_carrier_override(str(self.ui.sCarrierTxt.text()))
            else:
                self.status_manager.unset_secondary_carrier_override()
    def on_sCarrierTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.sCarrierChk.isChecked():
                self.status_manager.set_secondary_carrier_override(text)
    def on_sBadgeChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_secondary_service_badge(str(self.ui.sBadgeTxt.text()))
            else:
                self.status_manager.unset_secondary_service_badge()
    def on_sBadgeTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.sBadgeChk.isChecked():
                self.status_manager.set_secondary_service_badge(text)
    def on_sTypeChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_secondary_data_network_type(self.ui.sTypeDrp.currentIndex())
            else:
                self.status_manager.unset_secondary_data_network_type()
    def on_sTypeDrp_activated(self, index: int):
        if self.status_manager != None:
            if self.ui.sTypeChk.isChecked():
                self.status_manager.set_secondary_data_network_type(index)
    def on_sStrengthChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_secondary_gsm_signal_strength_bars(self.ui.sStrengthSld.value())
            else:
                self.status_manager.unset_secondary_gsm_signal_strength_bars()
    def on_sStrengthSld_sliderMoved(self, pos: int):
        self.ui.sStrengthLbl.setText(str(pos) + (" Bar" if pos == 1 else " Bars"))
        if self.status_manager != None:
            if self.ui.sStrengthChk.isChecked():
                self.status_manager.set_secondary_gsm_signal_strength_bars(pos)

    # Misc Text Inputs
    def on_timeChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_time(self.ui.timeTxt.text())
            else:
                self.status_manager.unset_time()
    def on_timeTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.timeChk.isChecked():
                self.status_manager.set_time(text)

    def on_breadcrumbChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_crumb(self.ui.breadcrumbTxt.text())
            else:
                self.status_manager.unset_crumb()
    def on_breadcrumbTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.breadcrumbChk.isChecked():
                self.status_manager.set_crumb(text)

    def on_batteryDetailChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_battery_detail(self.ui.batteryDetailTxt.text())
            else:
                self.status_manager.unset_battery_detail()
    def on_batteryDetailTxt_textEdited(self, text: str):
        if self.status_manager != None:
            if self.ui.batteryDetailChk.isChecked():
                self.status_manager.set_battery_detail(text)

    # Misc Slider Inputs
    def on_batteryCapacityChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_battery_capacity(self.ui.batteryCapacitySld.value())
            else:
                self.status_manager.unset_battery_capacity()
    def on_batteryCapacitySld_sliderMoved(self, pos: int):
        self.ui.batteryCapacityLbl.setText(str(pos) + "%")
        if self.status_manager != None:
            if self.ui.batteryCapacityChk.isChecked():
                self.status_manager.set_battery_capacity(pos)

    def on_wifiStrengthChk_clicked(self, checked: bool):
        if self.status_manager != None:
            if checked:
                self.status_manager.set_wifi_signal_strength_bars(self.ui.wifiStrengthSld.value())
            else:
                self.status_manager.unset_wifi_signal_strength_bars()
    def on_wifiStrengthSld_sliderMoved(self, pos: int):
        self.ui.wifiStrengthLbl.setText(str(pos) + (" Bar" if pos == 1 else " Bars"))
        if self.status_manager != None:
            if self.ui.wifiStrengthChk.isChecked():
                self.status_manager.set_wifi_signal_strength_bars(pos)

    # Raw Signal Strength Inputs
    def on_numericWifiChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.show_raw_wifi_signal(checked)
    def on_numericCellChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.show_raw_gsm_signal(checked)

    # Hiding Option Inputs
    def on_hideDNDChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_dnd(checked)
    def on_hideAirplaneChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_airplane(checked)
    def on_hideWifiChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_wifi(checked)
    def on_hideBatteryChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_battery(checked)
    def on_hideBluetoothChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_bluetooth(checked)
    def on_hideAlarmChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_alarm(checked)
    def on_hideLocationChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_location(checked)
    def on_hideRotationChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_rotation(checked)
    def on_hideAirPlayChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_airplay(checked)
    def on_hideCarPlayChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_carplay(checked)
    def on_hideVPNChk_clicked(self, checked: bool):
        if self.status_manager != None:
            self.status_manager.hide_vpn(checked)

        
    ## LOADING STATUS BAR
    def load_status_bar(self):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            self.status_manager = None
            return
        self.status_manager = StatusSetter(self.device_manager.get_current_device_version(), ws)
        if self.status_manager == None:
            return
        # Load primary carrier settings
        if self.status_manager.is_cellular_service_overridden():
            if self.status_manager.get_cellular_service_override():
                self.ui.pShowRdo.setChecked(True)
            else:
                self.ui.pHideRdo.setChecked(True)
        else:
            self.ui.pDefaultRdo.setChecked(True)
        self.ui.pCarrierChk.setChecked(self.status_manager.is_carrier_overridden())
        self.ui.pCarrierTxt.setText(self.status_manager.get_carrier_override())
        self.ui.pBadgeChk.setChecked(self.status_manager.is_primary_service_badge_overridden())
        self.ui.pBadgeTxt.setText(self.status_manager.get_primary_service_badge_override())
        self.ui.pTypeChk.setChecked(self.status_manager.is_data_network_type_overridden())
        self.ui.pTypeDrp.setCurrentIndex(self.status_manager.get_data_network_type_override())
        self.ui.pStrengthChk.setChecked(self.status_manager.is_gsm_signal_strength_bars_overridden())
        pos: int = self.status_manager.get_gsm_signal_strength_bars_override()
        self.ui.pStrengthSld.setValue(pos)
        self.ui.pStrengthLbl.setText(str(pos) + (" Bar" if pos == 1 else " Bars"))

        # Load secondary carrier settings
        if self.status_manager.is_secondary_cellular_service_overridden():
            if self.status_manager.get_secondary_cellular_service_override():
                self.ui.sShowRdo.setChecked(True)
            else:
                self.ui.sHideRdo.setChecked(True)
        else:
            self.ui.sDefaultRdo.setChecked(True)
        self.ui.sCarrierChk.setChecked(self.status_manager.is_secondary_carrier_overridden())
        self.ui.sCarrierTxt.setText(self.status_manager.get_secondary_carrier_override())
        self.ui.sBadgeChk.setChecked(self.status_manager.is_secondary_service_badge_overridden())
        self.ui.sBadgeTxt.setText(self.status_manager.get_secondary_service_badge_override())
        self.ui.sTypeChk.setChecked(self.status_manager.is_secondary_data_network_type_overridden())
        self.ui.sTypeDrp.setCurrentIndex(self.status_manager.get_secondary_data_network_type_override())
        self.ui.sStrengthChk.setChecked(self.status_manager.is_secondary_gsm_signal_strength_bars_overridden())
        pos = self.status_manager.get_secondary_gsm_signal_strength_bars_override()
        self.ui.sStrengthSld.setValue(pos)
        self.ui.sStrengthLbl.setText(str(pos) + (" Bar" if pos == 1 else " Bars"))

        # Load misc text inputs
        self.ui.timeChk.setChecked(self.status_manager.is_time_overridden())
        self.ui.timeTxt.setText(self.status_manager.get_time_override())
        self.ui.breadcrumbChk.setChecked(self.status_manager.is_crumb_overridden())
        self.ui.breadcrumbTxt.setText(self.status_manager.get_crumb_override())
        self.ui.batteryDetailChk.setChecked(self.status_manager.is_battery_detail_overridden())
        self.ui.batteryDetailTxt.setText(self.status_manager.get_battery_detail_override())

        # Load misc slider inputs
        self.ui.batteryCapacityChk.setChecked(self.status_manager.is_battery_capacity_overridden())
        pos = self.status_manager.get_battery_capacity_override()
        self.ui.batteryCapacitySld.setValue(pos)
        self.ui.batteryCapacityLbl.setText(str(pos) + "%")
        self.ui.wifiStrengthChk.setChecked(self.status_manager.is_wifi_signal_strength_bars_overridden())
        pos = self.status_manager.get_wifi_signal_strength_bars_override()
        self.ui.wifiStrengthSld.setValue(pos)
        self.ui.wifiStrengthLbl.setText(str(pos) + (" Bar" if pos == 1 else " Bars"))

        # Load raw signal strength inputs
        self.ui.numericWifiChk.setChecked(self.status_manager.is_raw_wifi_signal_shown())
        self.ui.numericCellChk.setChecked(self.status_manager.is_raw_gsm_signal_shown())

        # Load hiding option inputs
        self.ui.hideDNDChk.setChecked(self.status_manager.is_dnd_hidden())
        self.ui.hideAirplaneChk.setChecked(self.status_manager.is_airplane_hidden())
        self.ui.hideWifiChk.setChecked(self.status_manager.is_wifi_hidden())
        self.ui.hideBatteryChk.setChecked(self.status_manager.is_battery_hidden())
        self.ui.hideBluetoothChk.setChecked(self.status_manager.is_bluetooth_hidden())
        self.ui.hideAlarmChk.setChecked(self.status_manager.is_alarm_hidden())
        self.ui.hideLocationChk.setChecked(self.status_manager.is_location_hidden())
        self.ui.hideRotationChk.setChecked(self.status_manager.is_rotation_hidden())
        self.ui.hideAirPlayChk.setChecked(self.status_manager.is_airplay_hidden())
        self.ui.hideCarPlayChk.setChecked(self.status_manager.is_carplay_hidden())
        self.ui.hideVPNChk.setChecked(self.status_manager.is_vpn_hidden())
        
    
    ## SPRINGBOARD OPTIONS PAGE
    def on_springboardOptionsEnabledChk_toggled(self, checked: bool):
        self.ui.springboardOptionsPageContent.setDisabled(not checked)
        self.device_manager.data_singleton.set_tweak_enabled(tweak=Tweak.SpringboardOptions, enabled=checked)
        self.update_enabled_tweaks()

    def on_UIAnimSpeedSld_sliderMoved(self, pos: int):
        speed = pos / 100.0
        speed_txt = "Default" if speed == 1 else "Slow" if speed > 1 else "Fast"
        self.ui.UIAnimSpeedLbl.setText(f"{speed} ({speed_txt})")
        # if the workspace exists, update the file
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, FileLocation.uikit.value)
        if speed != 1:
            set_plist_value(location, "UIAnimationDragCoefficient", speed)
        else:
            delete_plist_key(location, "UIAnimationDragCoefficient")

    def on_footnoteTxt_textEdited(self, text: str):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, FileLocation.footnote.value)
        if text != "":
            set_plist_value(location, "LockScreenFootnote", text)
        else:
            delete_plist_key(location, "LockScreenFootnote")

    def on_disableLockRespringChk_clicked(self, checked: bool):
        self.set_key("SBDontLockAfterCrash", checked, FileLocation.springboard)
    def on_disableBatteryAlertsChk_clicked(self, checked: bool):
        self.set_key("SBHideLowPowerAlerts", checked, FileLocation.springboard)
    def on_disableDimmingChk_clicked(self, checked: bool):
        self.set_key("SBDontDimOrLockOnAC", checked, FileLocation.springboard)
    def on_disableCrumbChk_clicked(self, checked: bool):
        self.set_key("SBNeverBreadcrumb", checked, FileLocation.springboard)
    def on_enableSupervisionTextChk_clicked(self, checked: bool):
        self.set_key("SBShowSupervisionTextOnLockScreen", checked, FileLocation.springboard)
    def on_enableWiFiDebuggerChk_clicked(self, checked: bool):
        self.set_key("WiFiManagerLoggingEnabled", checked, FileLocation.wifi_debug)
    def on_enableShutdownSoundChk_clicked(self, checked: bool):
        self.set_sb_key("Accessibility", checked, FileLocation.accessibility)

    def on_allowAirDropEveryoneChk_clicked(self, checked: bool):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, FileLocation.airdrop.value)
        if checked:
            set_plist_value(location, "DiscoverableMode", "Everyone")
        else:
            delete_plist_key(location, "DiscoverableMode")


    ## LOADING SPRINGBOARD OPTIONS
    def load_springboard_options(self):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        # load all the files
        location = os.path.join(ws, FileLocation.uikit.value)
        value = get_plist_value(location, "UIAnimationDragCoefficient")
        if value != None:
            speed_txt = "Default" if value == 1 else "Slow" if value > 1 else "Fast"
            self.ui.UIAnimSpeedLbl.setText(f"{value} ({speed_txt})")
            self.ui.UIAnimSpeedSld.setValue(value * 100)
        else:
            self.ui.UIAnimSpeedLbl.setText("1 (Default)")
            self.ui.UIAnimSpeedSld.setValue(100)
        location = os.path.join(ws, FileLocation.footnote.value)
        value = get_plist_value(location, "LockScreenFootnote")
        self.ui.footnoteTxt.setText("" if value == None else str(value))

        location = os.path.join(ws, FileLocation.springboard.value)
        value = get_plist_value(location, "SBDontLockAfterCrash")
        self.ui.disableLockRespringChk.setChecked(value if value else False)
        value = get_plist_value(location, "SBDontDimOrLockOnAC")
        self.ui.disableDimmingChk.setChecked(value if value else False)
        value = get_plist_value(location, "SBHideLowPowerAlerts")
        self.ui.disableBatteryAlertsChk.setChecked(value if value else False)
        value = get_plist_value(location, "SBNeverBreadcrumb")
        self.ui.disableCrumbChk.setChecked(value if value else False)
        value = get_plist_value(location, "SBShowSupervisionTextOnLockScreen")
        self.ui.enableSupervisionTextChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.wifi_debug.value)
        value = get_plist_value(location, "WiFiManagerLoggingEnabled")
        self.ui.enableWiFiDebuggerChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.accessibility.value)
        value = get_plist_value(location, "StartupSoundEnabled")
        self.ui.enableShutdownSoundChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.airdrop.value)
        value = get_plist_value(location, "DiscoverableMode")
        self.ui.allowAirDropEveryoneChk.setChecked(value if value == "Everyone" else False)


    ## INTERNAL OPTIONS PAGE
    def on_internalOptionsEnabledChk_toggled(self, checked: bool):
        self.ui.internalOptionsPageContent.setDisabled(not checked)
        self.device_manager.data_singleton.set_tweak_enabled(tweak=Tweak.InternalOptions, enabled=checked)
        self.update_enabled_tweaks()

    def on_buildVersionChk_clicked(self, checked: bool):
        self.set_key("UIStatusBarShowBuildVersion", checked, FileLocation.global_prefs)
    def on_RTLChk_clicked(self, checked: bool):
        self.set_key("NSForceRightToLeftWritingDirection", checked, FileLocation.global_prefs)
    def on_metalHUDChk_clicked(self, checked: bool):
        self.set_key("MetalForceHudEnabled", checked, FileLocation.global_prefs)
    def on_accessoryChk_clicked(self, checked: bool):
        self.set_key("AccessoryDeveloperEnabled", checked, FileLocation.global_prefs)
    def on_iMessageChk_clicked(self, checked: bool):
        self.set_key("iMessageDiagnosticsEnabled", checked, FileLocation.global_prefs)
    def on_IDSChk_clicked(self, checked: bool):
        self.set_key("IDSDiagnosticsEnabled", checked, FileLocation.global_prefs)
    def on_VCChk_clicked(self, checked: bool):
        self.set_key("VCDiagnosticsEnabled", checked, FileLocation.global_prefs)

    def on_appStoreChk_clicked(self, checked: bool):
        self.set_key("debugGestureEnabled", checked, FileLocation.app_store)
    def on_notesChk_clicked(self, checked: bool):
        self.set_key("DebugModeEnabled", checked, FileLocation.notes)

    def on_showTouchesChk_clicked(self, checked: bool):
        self.set_key("BKDigitizerVisualizeTouches", checked, FileLocation.backboardd)
    def on_hideRespringChk_clicked(self, checked: bool):
        self.set_key("BKHideAppleLogoOnLaunch", checked, FileLocation.backboardd)
    def on_enableWakeVibrateChk_clicked(self, checked: bool):
        self.set_key("EnableWakeGestureHaptic", checked, FileLocation.core_motion)
    def on_pasteSoundChk_clicked(self, checked: bool):
        self.set_key("PlaySoundOnPaste", checked, FileLocation.pasteboard)
    def on_notifyPastesChk_clicked(self, checked: bool):
        self.set_key("AnnounceAllPastes", checked, FileLocation.pasteboard)


    ## LOADING INTERNAL OPTIONS
    def load_internal_options(self):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        # load all the files
        location = os.path.join(ws, FileLocation.global_prefs.value)
        value = get_plist_value(location, "UIStatusBarShowBuildVersion")
        self.ui.buildVersionChk.setChecked(value if value else False)
        value = get_plist_value(location, "NSForceRightToLeftWritingDirection")
        self.ui.RTLChk.setChecked(value if value else False)
        value = get_plist_value(location, "MetalForceHudEnabled")
        self.ui.metalHUDChk.setChecked(value if value else False)
        value = get_plist_value(location, "AccessoryDeveloperEnabled")
        self.ui.accessoryChk.setChecked(value if value else False)
        value = get_plist_value(location, "iMessageDiagnosticsEnabled")
        self.ui.iMessageChk.setChecked(value if value else False)
        value = get_plist_value(location, "IDSDiagnosticsEnabled")
        self.ui.IDSChk.setChecked(value if value else False)
        value = get_plist_value(location, "VCDiagnosticsEnabled")
        self.ui.VCChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.app_store.value)
        value = get_plist_value(location, "debugGestureEnabled")
        self.ui.appStoreChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.notes.value)
        value = get_plist_value(location, "DebugModeEnabled")
        self.ui.notesChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.backboardd.value)
        value = get_plist_value(location, "BKDigitizerVisualizeTouches")
        self.ui.showTouchesChk.setChecked(value if value else False)
        value = get_plist_value(location, "BKHideAppleLogoOnLaunch")
        self.ui.hideRespringChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.core_motion.value)
        value = get_plist_value(location, "EnableWakeGestureHaptic")
        self.ui.enableWakeVibrateChk.setChecked(value if value else False)

        location = os.path.join(ws, FileLocation.pasteboard.value)
        value = get_plist_value(location, "PlaySoundOnPaste")
        self.ui.pasteSoundChk.setChecked(value if value else False)
        value = get_plist_value(location, "AnnounceAllPastes")
        self.ui.notifyPastesChk.setChecked(value if value else False)


    ## SETUP OPTIONS PAGE
    def on_setupOptionsEnabledChk_toggled(self, checked: bool):
        self.ui.setupOptionsPageContent.setDisabled(not checked)
        self.device_manager.data_singleton.set_tweak_enabled(tweak=Tweak.SkipSetup, enabled=checked)
        self.update_enabled_tweaks()

    def on_skipSetupChk_clicked(self, checked: bool):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, FileLocation.cloud_config.value)
        if checked:
            set_plist_value(location, "CloudConfigurationUIComplete", True)
            to_skip = [
                "Location",
                "Restore",
                "SIMSetup",
                "Android",
                "AppleID",
                "IntendedUser",
                "TOS",
                "Siri",
                "ScreenTime",
                "Diagnostics",
                "SoftwareUpdate",
                "Passcode",
                "Biometric",
                "Payment",
                "Zoom",
                "DisplayTone",
                "MessagingActivationUsingPhoneNumber",
                "HomeButtonSensitivity",
                "CloudStorage",
                "ScreenSaver",
                "TapToSetup",
                "Keyboard",
                "PreferredLanguage",
                "SpokenLanguage",
                "WatchMigration",
                "OnBoarding",
                "TVProviderSignIn",
                "TVHomeScreenSync",
                "Privacy",
                "TVRoom",
                "iMessageAndFaceTime",
                "AppStore",
                "Safety",
                "Multitasking",
                "ActionButton",
                "TermsOfAddress",
                "AccessibilityAppearance",
                "Welcome",
                "Appearance",
                "RestoreCompleted",
                "UpdateCompleted"
            ]
            set_plist_value(location, "SkipSetup", to_skip)
        else:
            delete_plist_key(location, "SkipSetup")
        
    def on_enableSupervisionChk_clicked(self, checked: bool):
        self.set_key("IsSupervised", checked, FileLocation.cloud_config)

    def on_organizationNameTxt_textEdited(self, text: str):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, FileLocation.cloud_config.value)
        if text != "":
            set_plist_value(location, "OrganizationName", text)
        else:
            delete_plist_key(location, "OrganizationName")


    ## LOADING SETUP OPTIONS
    def load_setup_options(self):
        ws = self.device_manager.data_singleton.current_workspace
        # load all the files
        location = os.path.join(ws, FileLocation.cloud_config.value)
        skip_setup = get_plist_value(location, "SkipSetup")
        is_supervised = get_plist_value(location, "IsSupervised")
        org_name = get_plist_value(location, "OrganizationName")
        self.ui.skipSetupChk.setDisabled(skip_setup == None)
        self.ui.enableSupervisionChk.setDisabled(True if is_supervised == None else False)
        self.ui.organizationNameTxt.setText("" if org_name == None else str(org_name))

    
    
    ## APPLY PAGE
    def update_label(self, txt: str):
        self.ui.statusLbl.setText(txt)
        if "Restoring" in txt:
            self.ui.restoreProgressBar.setValue(0)
            self.ui.restoreProgressBar.show()
    def update_bar(self, percent):
        self.ui.restoreProgressBar.setValue(int(percent))
    def on_removeTweaksBtn_clicked(self):
        # TODO: Add safety here
        self.device_manager.remove_tweaks(deep_clean=False, update_label=self.update_label, update_bar=self.update_bar)

    def on_deepCleanBtn_clicked(self):
        # TODO: Add safety here
        self.device_manager.remove_tweaks(deep_clean=True, update_label=self.update_label, update_bar=self.update_bar)

    @QtCore.Slot()
    def on_applyTweaksBtn_clicked(self):
        # TODO: Add safety here
        self.device_manager.apply_tweaks(update_label=self.update_label, update_bar=self.update_bar)
