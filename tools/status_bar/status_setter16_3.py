from ctypes import Structure, c_bool, c_char, c_int, c_uint, c_double, sizeof, create_string_buffer, memmove
import os

from devicemanagement.constants import FileLocation

class StatusBarRawData(Structure):
    _fields_ = [
        ("itemIsEnabled", c_bool * 45),
        ("padding1", c_char),
        ("padding2", c_char),
        ("timeString", c_char * 64),
        ("shortTimeString", c_char * 64),
        ("dateString", c_char * 256),
        ("gsmSignalStrengthRaw", c_int),
        ("secondaryGsmSignalStrengthRaw", c_int),
        ("gsmSignalStrengthBars", c_int),
        ("secondaryGsmSignalStrengthBars", c_int),
        ("serviceString", c_char * 100),
        ("secondaryServiceString", c_char * 100),
        ("serviceCrossfadeString", c_char * 100),
        ("secondaryServiceCrossfadeString", c_char * 100),
        ("serviceImages", c_char * 2 * 100),
        ("operatorDirectory", c_char * 1024),
        ("serviceContentType", c_uint),
        ("secondaryServiceContentType", c_uint),
        ("cellLowDataModeActive", c_uint, 1),
        ("secondaryCellLowDataModeActive", c_uint, 1),
        ("wifiSignalStrengthRaw", c_int),
        ("wifiSignalStrengthBars", c_int),
        ("wifiLowDataModeActive", c_uint, 1),
        ("dataNetworkType", c_uint),
        ("secondaryDataNetworkType", c_uint),
        ("batteryCapacity", c_int),
        ("batteryState", c_uint),
        ("batteryDetailString", c_char * 150),
        ("bluetoothBatteryCapacity", c_int),
        ("thermalColor", c_int),
        ("thermalSunlightMode", c_uint, 1),
        ("slowActivity", c_uint, 1),
        ("syncActivity", c_uint, 1),
        ("activityDisplayId", c_char * 256),
        ("bluetoothConnected", c_uint, 1),
        ("displayRawGSMSignal", c_uint, 1),
        ("displayRawWifiSignal", c_uint, 1),
        ("locationIconType", c_uint, 1),
        ("voiceControlIconType", c_uint, 2),
        ("quietModeInactive", c_uint, 1),
        ("tetheringConnectionCount", c_uint),
        ("batterySaverModeActive", c_uint, 1),
        ("deviceIsRTL", c_uint, 1),
        ("lock", c_uint, 1),
        ("breadcrumbTitle", c_char * 256),
        ("breadcrumbSecondaryTitle", c_char * 256),
        ("personName", c_char * 100),
        ("electronicTollCollectionAvailable", c_uint, 1),
        ("radarAvailable", c_uint, 1),
        ("wifiLinkWarning", c_uint, 1),
        ("wifiSearching", c_uint, 1),
        ("backgroundActivityDisplayStartDate", c_double),
        ("shouldShowEmergencyOnlyStatus", c_uint, 1),
        ("secondaryCellularConfigured", c_uint, 1),
        ("primaryServiceBadgeString", c_char * 100),
        ("secondaryServiceBadgeString", c_char * 100),
        ("quietModeImage", c_char * 256),
        ("extra1", c_uint, 1)
    ]
# End of StatusBarRawData struct

class StatusBarOverrideData(Structure):
    _fields_ = [
        ("overrideItemIsEnabled", c_bool * 45),
        ("padding1", c_char),
        ("overrideTimeString", c_uint, 1),
        ("overrideDateString", c_uint, 1),
        ("overrideGsmSignalStrengthRaw", c_uint, 1),
        ("overrideSecondaryGsmSignalStrengthRaw", c_uint, 1),
        ("overrideGsmSignalStrengthBars", c_uint, 1),
        ("overrideSecondaryGsmSignalStrengthBars", c_uint, 1),
        ("overrideServiceString", c_uint, 1),
        ("overrideSecondaryServiceString", c_uint, 1),
        ("overrideServiceImages", c_uint, 2),
        ("overrideOperatorDirectory", c_uint, 1),
        ("overrideServiceContentType", c_uint, 1),
        ("overrideSecondaryServiceContentType", c_uint, 1),
        ("overrideWifiSignalStrengthRaw", c_uint, 1),
        ("overrideWifiSignalStrengthBars", c_uint, 1),
        ("overrideDataNetworkType", c_uint, 1),
        ("overrideSecondaryDataNetworkType", c_uint, 1),
        ("disallowsCellularDataNetworkTypes", c_uint, 1),
        ("overrideBatteryCapacity", c_uint, 1),
        ("overrideBatteryState", c_uint, 1),
        ("overrideBatteryDetailString", c_uint, 1),
        ("overrideBluetoothBatteryCapacity", c_uint, 1),
        ("overrideThermalColor", c_uint, 1),
        ("overrideSlowActivity", c_uint, 1),
        ("overrideActivityDisplayId", c_uint, 1),
        ("overrideBluetoothConnected", c_uint, 1),
        ("overrideBreadcrumb", c_uint, 1),
        ("overrideLock", c_uint),
        ("overrideDisplayRawGSMSignal", c_uint, 1),
        ("overrideDisplayRawWifiSignal", c_uint, 1),
        ("overridePersonName", c_uint, 1),
        ("overrideWifiLinkWarning", c_uint, 1),
        ("overrideSecondaryCellularConfigured", c_uint, 1),
        ("overridePrimaryServiceBadgeString", c_uint, 1),
        ("overrideSecondaryServiceBadgeString", c_uint, 1),
        ("overrideQuietModeImage", c_uint, 1),
        ("overrideExtra1", c_uint, 1),
        ("values", StatusBarRawData)
    ]
# End of StatusBarOverrideData struct
    
class Setter:
    def __init__(self, workspace: str):
        self.ws = workspace

    def apply_changes(self, overrides: StatusBarOverrideData):
        path = os.join(self.ws, FileLocation.status_bar.value)
        try:
            with open(path, "wb") as out_file:
                out_file.write(overrides)
                padding = create_string_buffer(256)
                padding.raw = b'\0' * 256
                out_file.write(padding)
        except IOError:
            print(f"Failed to open file: {path}")

    def get_overrides(self) -> StatusBarOverrideData:
        path = os.path.join(self.ws, FileLocation.status_bar.value)
        overrides = StatusBarOverrideData()
        if os.path.exists(path):
            # read and map the file
            try:
                with open(path, "rb") as in_file:
                    in_file.readinto(overrides)
            except IOError:
                print(f"Failed to open file: {path}")
        return overrides