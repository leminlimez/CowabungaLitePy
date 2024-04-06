import tools.status_bar.status_setter16_3 as status_setter16_3
from devicemanagement.constants import Version

class StatusSetter:
    def __init__(self, version: str, workspace: str):
        parsed_ver: Version = Version(version)
        if parsed_ver >= Version("16.3"):
            self.setter = status_setter16_3.Setter(workspace)

        
    ### PRIMARY CARRIER
    # CELLULAR SERVICE
    def is_cellular_service_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def get_cellular_service_override(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] == 1
    def set_cellular_service(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_cellular_service(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularServiceStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
            
    # SERVICE STRING
    def is_carrier_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideServiceString == 1
    def get_carrier_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.serviceString.decode()
    def set_carrier_override(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideServiceString = 1
        overrides.values.serviceString = text.encode()
        overrides.values.serviceCrossfadeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_carrier_override(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideServiceString = 0
        self.setter.apply_changes(overrides)

    # SERVICE BADGE
    def is_primary_service_badge_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overridePrimaryServiceBadgeString == 1
    def get_primary_service_badge_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.primaryServiceBadgeString.decode()
    def set_primary_service_badge(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overridePrimaryServiceBadgeString = 1
        overrides.values.primaryServiceBadgeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_primary_service_badge(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overridePrimaryServiceBadgeString = 0
        self.setter.apply_changes(overrides)

    # DATA NETWORK TYPE
    def is_data_network_type_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDataNetworkType == 1
    def get_data_network_type_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.dataNetworkType
    def set_data_network_type(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDataNetworkType = 1
        overrides.values.dataNetworkType = id
        self.setter.apply_changes(overrides)
    def unset_data_network_type(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDataNetworkType = 0
        self.setter.apply_changes(overrides)

    # GSM SIGNAL BARS
    def is_gsm_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideGSMSignalStrengthBars == 1
    def get_gsm_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.GSMSignalStrengthBars
    def set_gsm_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 1
        overrides.overrideGSMSignalStrengthBars = 1
        overrides.values.GSMSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_gsm_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.CellularSignalStrengthStatusBarItem.value] = 0
        overrides.overrideGSMSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ### SECONDARY CARRIER
    # CELLULAR SERVICE
    def is_secondary_cellular_service_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] == 1
    def get_secondary_cellular_service_override(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.values.itemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] == 1
    def set_secondary_cellular_service(self, shown: bool) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 1 if shown else 0
        self.setter.apply_changes(overrides)
    def unset_secondary_cellular_service(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularServiceStatusBarItem.value] = 0
        self.setter.apply_changes(overrides)
            
    # SERVICE STRING
    def is_secondary_carrier_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryServiceString == 1
    def get_secondary_carrier_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryServiceString.decode()
    def set_secondary_carrier_override(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceString = 1
        overrides.values.secondaryServiceString = text.encode()
        overrides.values.secondaryServiceCrossfadeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_secondary_carrier_override(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceString = 0
        self.setter.apply_changes(overrides)

    # SERVICE BADGE
    def is_secondary_service_badge_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryServiceBadgeString == 1
    def get_secondary_service_badge_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryServiceBadgeString.decode()
    def set_secondary_service_badge(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceBadgeString = 1
        overrides.values.secondaryServiceBadgeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_secondary_service_badge(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryServiceBadgeString = 0
        self.setter.apply_changes(overrides)

    # DATA NETWORK TYPE
    def is_secondary_data_network_type_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryDataNetworkType == 1
    def get_secondary_data_network_type_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryDataNetworkType
    def set_secondary_data_network_type(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryDataNetworkType = 1
        overrides.values.secondaryDataNetworkType = id
        self.setter.apply_changes(overrides)
    def unset_secondary_data_network_type(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideSecondaryDataNetworkType = 0
        self.setter.apply_changes(overrides)

    # GSM SIGNAL BARS
    def is_secondary_gsm_signal_strength_bars_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideSecondaryGSMSignalStrengthBars == 1
    def get_secondary_gsm_signal_strength_bars_override(self) -> int:
        overrides = self.setter.get_overrides()
        return overrides.values.secondaryGSMSignalStrengthBars
    def set_secondary_gsm_signal_strength_bars(self, id: int) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 1
        overrides.values.itemIsEnabled[self.setter.StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 1
        overrides.overrideSecondaryGSMSignalStrengthBars = 1
        overrides.values.secondaryGSMSignalStrengthBars = id
        self.setter.apply_changes(overrides)
    def unset_secondary_gsm_signal_strength_bars(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideItemIsEnabled[self.setter.StatusBarItem.SecondaryCellularSignalStrengthStatusBarItem.value] = 0
        overrides.overrideSecondaryGSMSignalStrengthBars = 0
        self.setter.apply_changes(overrides)


    ### MISC TEXT INPUTS
    # DATE STRING (Unused)
    def is_date_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideDateString == 1
    def get_date_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.dateString.decode()
    def set_date(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDateString = 1
        overrides.values.dateString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_date(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideDateString = 0
        self.setter.apply_changes(overrides)

    # TIME STRING
    def is_time_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideTimeString == 1
    def get_time_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.timeString.decode()
    def set_time(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideTimeString = 1
        overrides.values.timeString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_time(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideTimeString = 0
        self.setter.apply_changes(overrides)

    # BREADCRUMB STRING
    def is_crumb_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBreadcrumb == 1
    def get_crumb_override(self) -> str:
        overrides = self.setter.get_overrides()
        text: str = overrides.values.breadcrumbTitle.decode()
        if len(text) > 1:
            return text[:len(text) - 4]
        return ""
    def set_crumb(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBreadcrumb = 1
        new_crumb = ""
        if text != "":
            new_crumb: str = text + " ▶"
        overrides.values.breadcrumbTitle = new_crumb.encode()
        self.setter.apply_changes(overrides)
    def unset_crumb(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBreadcrumb = 0
        overrides.values.breadcrumbTitle = "".encode()
        self.setter.apply_changes(overrides)

    # BATTERY DETAIL STRING
    def is_battery_detail_overridden(self) -> bool:
        overrides = self.setter.get_overrides()
        return overrides.overrideBatteryDetailString == 1
    def get_battery_detail_override(self) -> str:
        overrides = self.setter.get_overrides()
        return overrides.values.batteryDetailString.decode()
    def set_battery_detail(self, text: str) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryDetailString = 1
        overrides.values.batteryDetailString = text.encode()
        self.setter.apply_changes(overrides)
    def unset_battery_detail(self) -> None:
        overrides = self.setter.get_overrides()
        overrides.overrideBatteryDetailString = 0
        self.setter.apply_changes(overrides)
