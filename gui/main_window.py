from PySide6 import QtCore, QtWidgets
from enum import Enum
from pathlib import Path
import webbrowser
import os

from pymobiledevice3.lockdown import create_using_usbmux

from ui_mainwindow import Ui_CowabungaLite

from devicemanagement.constants import Version, Tweak
from devicemanagement.device_manager import DeviceManager

from tools.locsim import mount_dev_disk, LocSimManager

from utils.plist_manager import get_plist_value, set_plist_value, delete_plist_key

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
        self.locsim_manager: LocSimManager = None

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

        ## SETUP OPTIONS PAGE
        self.ui.setupOptionsEnabledChk.toggled.connect(self.on_setupOptionsEnabledChk_toggled)
        self.ui.skipSetupChk.toggled.connect(self.on_skipSetupChk_clicked)
        self.ui.enableSupervisionChk.toggled.connect(self.on_enableSupervisionChk_clicked)
        self.ui.organizationNameTxt.textEdited.connect(self.on_organizationNameTxt_textEdited)

        ## APPLY PAGE ACTIONS
        self.ui.applyTweaksBtn.clicked.connect(self.on_applyPageBtn_clicked)


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
            self.location_loading = False

            # TODO: Load Pages
            self.load_springboard_options()
            self.load_setup_options()
        
        # TODO: update enabled tweaks
        self.update_enabled_tweaks()

    def update_enabled_tweaks(self):
        tweaks = self.device_manager.data_singleton.enabled_tweaks
        label_txt = ""
        if len(tweaks) == 0:
            label_txt = "None"
            self.ui.applyPage.setDisabled(True)
        else:
            first_tweak: bool = True
            for tweak in tweaks:
                if not first_tweak:
                    label_txt += ", "
                else:
                    first_tweak = False
                label_txt += tweak.value
            self.ui.applyPage.setDisabled(False)
            
        self.ui.enabledTweaksLbl.setText(label_txt)

        #self.ui.themesEnabledChk.setChecked()
        #self.ui.statusBarEnabledChk.setChecked()
        self.ui.springboardOptionsEnabledChk.setChecked(Tweak.SpringboardOptions in tweaks)
        #self.ui.internalOptionsEnabledChk.setChecked()
        self.ui.setupOptionsEnabledChk.setChecked(Tweak.SkipSetup in tweaks)


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
        location = os.path.join(ws, "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.UIKit.plist")
        if speed != 1:
            set_plist_value(location, "UIAnimationDragCoefficient", speed)
        else:
            delete_plist_key(location, "UIAnimationDragCoefficient")

    ## LOADING SPRINGBOARD OPTIONS
    def load_springboard_options(self):
        ws = self.device_manager.data_singleton.current_workspace
        # load all the files
        location = os.path.join(ws, "SpringboardOptions/ManagedPreferencesDomain/mobile/com.apple.UIKit.plist")
        value = get_plist_value(location, "UIAnimationDragCoefficient")
        if value != None:
            speed_txt = "Default" if value == 1 else "Slow" if value > 1 else "Fast"
            self.ui.UIAnimSpeedLbl.setText(f"{value} ({speed_txt})")
            self.ui.UIAnimSpeedSld.setValue(value * 100)
        else:
            self.ui.UIAnimSpeedLbl.setText("1 (Default)")
            self.ui.UIAnimSpeedSld.setValue(100)


    ## SETUP OPTIONS PAGE
    def on_setupOptionsEnabledChk_toggled(self, checked: bool):
        self.ui.setupOptionsPageContent.setDisabled(not checked)
        self.device_manager.data_singleton.set_tweak_enabled(tweak=Tweak.SkipSetup, enabled=checked)
        self.update_enabled_tweaks()

    def on_skipSetupChk_clicked(self, checked: bool):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, "SkipSetup/ConfigProfileDomain/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
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
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, "SkipSetup/ConfigProfileDomain/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
        if checked:
            set_plist_value(location, "IsSupervised", True)
        else:
            delete_plist_key(location, "IsSupervised")

    def on_organizationNameTxt_textEdited(self, text: str):
        ws = self.device_manager.data_singleton.current_workspace
        if ws == None:
            return
        location = os.path.join(ws, "SkipSetup/ConfigProfileDomain/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
        if text != "":
            set_plist_value(location, "OrganizationName", text)
        else:
            delete_plist_key(location, "OrganizationName")


    ## LOADING SETUP OPTIONS
    def load_setup_options(self):
        ws = self.device_manager.data_singleton.current_workspace
        # load all the files
        location = os.path.join(ws, "SkipSetup/ConfigProfileDomain/Library/ConfigurationProfiles/CloudConfigurationDetails.plist")
        skip_setup = get_plist_value(location, "SkipSetup")
        is_supervised = get_plist_value(location, "IsSupervised")
        org_name = get_plist_value(location, "OrganizationName")
        self.ui.skipSetupChk.setDisabled(skip_setup == None)
        self.ui.enableSupervisionChk.setDisabled(True if is_supervised == None else False)
        self.ui.organizationNameTxt.setText("" if org_name == None else str(org_name))

    
    
    ## APPLY PAGE
    @QtCore.Slot()
    def on_applyTweaksBtn_clicked(self):
        # TODO: Add safety here
        def update_label(txt: str):
            self.ui.statusLbl.setText(txt)
            if "Restoring" in txt:
                self.ui.restoreProgressBar.setValue(0)
                self.ui.restoreProgressBar.show()
        def update_bar(percent):
            self.ui.restoreProgressBar.setValue(int(percent))
        self.device_manager.apply_tweaks(update_label=update_label, update_bar=update_bar)