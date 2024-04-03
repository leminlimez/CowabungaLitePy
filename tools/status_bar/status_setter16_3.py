import cstruct
import os

from devicemanagement.constants import FileLocation

# class StatusBarItem(cstruct.CEnum):
#     __def__ = """
#         enum class StatusBarItem : int
#         {
#             TimeStatusBarItem = 0,
#             DateStatusBarItem = 1,
#             QuietModeStatusBarItem = 2,
#             AirplaneModeStatusBarItem = 3,
#             CellularSignalStrengthStatusBarItem = 4,
#             SecondaryCellularSignalStrengthStatusBarItem = 5,
#             CellularServiceStatusBarItem = 6,
#             SecondaryCellularServiceStatusBarItem = 7,
#             // 8
#             CellularDataNetworkStatusBarItem = 9,
#             SecondaryCellularDataNetworkStatusBarItem = 10,
#             // 11
#             MainBatteryStatusBarItem = 12,
#             ProminentlyShowBatteryDetailStatusBarItem = 13,
#             // 14
#             // 15
#             BluetoothStatusBarItem = 16,
#             TTYStatusBarItem = 17,
#             AlarmStatusBarItem = 18,
#             // 19
#             // 20
#             LocationStatusBarItem = 21,
#             RotationLockStatusBarItem = 22,
#             CameraUseStatusBarItem = 23,
#             AirPlayStatusBarItem = 24,
#             AssistantStatusBarItem = 25,
#             CarPlayStatusBarItem = 26,
#             StudentStatusBarItem = 27,
#             MicrophoneUseStatusBarItem = 28,
#             VPNStatusBarItem = 29,
#             // 30
#             // 31
#             // 32
#             // 33
#             // 34
#             // 35
#             // 36
#             // 37
#             LiquidDetectionStatusBarItem = 38,
#             VoiceControlStatusBarItem = 39,
#             // 40
#             // 41
#             // 42
#             // 43
#             Extra1StatusBarItem = 44
#         };
#     """
# # End of StatusBarItem enum
    
# class BatteryState(cstruct.CEnum):
#     __def__ = """
#     enum class BatteryState : unsigned int
#     {
#         BatteryStateUnplugged = 0
#     };
#     """

class StatusBarOverrideData(cstruct.MemCStruct):
    __byte_order__ = cstruct.NATIVE_ORDER
    __def__ = """
    struct StatusBarOverrideData {
        char overrideItemIsEnabled[45];
        char padding;
        unsigned int overrideTimeString;
        unsigned int overrideDateString;
        unsigned int overrideGSMSignalStrengthRaw;
        unsigned int overrideSecondaryGSMSignalStrengthRaw;
        unsigned int overrideGSMSignalStrengthBars;
        unsigned int overrideSecondaryGSMSignalStrengthBars;
        unsigned int overrideServiceString;
        unsigned int overrideSecondaryServiceString;
        unsigned int overrideServiceImages;
        unsigned int overrideOperatorDirectory;
        unsigned int overrideServiceContentType;
        unsigned int overrideSecondaryServiceContentType;
        unsigned int overrideWiFiSignalStrengthRaw;
        unsigned int overrideWiFiSignalStrengthBars;
        unsigned int overrideDataNetworkType;
        unsigned int overrideSecondaryDataNetworkType;
        unsigned int disallowsCellularDataNetworkTypes;
        unsigned int overrideBatteryCapacity;
        unsigned int overrideBatteryState;
        unsigned int overrideBatteryDetailString;
        unsigned int overrideBluetoothBatteryCapacity;
        unsigned int overrideThermalColor;
        unsigned int overrideSlowActivity;
        unsigned int overrideActivityDisplayId;
        unsigned int overrideBluetoothConnected;
        unsigned int overrideBreadcrumb;
        unsigned int overrideLock;
        unsigned int overrideDisplayRawGSMSignal;
        unsigned int overrideDisplayRawWiFiSignal;
        unsigned int overridePersonName;
        unsigned int overrideWiFiLinkWarning;
        unsigned int overrideSecondaryCellularConfigured;
        unsigned int overridePrimaryServiceBadgeString;
        unsigned int overrideSecondaryServiceBadgeString;
        unsigned int overrideQuietModeImage;
        unsigned int overrideExtra1;
        struct StatusBarRawData {
            char itemIsEnabled[45];
            char padding1;
            char padding2;
            char timeString[64];
            char shortTimeString[64];
            char dateString[256];
            int GSMSignalStrengthRaw;
            int secondaryGSMSignalStrengthRaw;
            int GSMSignalStrengthBars;
            int secondaryGSMSignalStrengthBars;
            char serviceString[100];
            char secondaryServiceString[100];
            char serviceCrossfadeString[100];
            char secondaryServiceCrossfadeString[100];
            char serviceImages[200];
            char operatorDirectory[1024];
            unsigned int serviceContentType;
            unsigned int secondaryServiceContentType;
            unsigned int cellLowDataModeActive;
            unsigned int secondaryCellLowDataModeActive;
            int WiFiSignalStrengthRaw;
            int WiFiSignalStrengthBars;
            unsigned int WiFiLowDataModeActive;
            unsigned int dataNetworkType;
            unsigned int secondaryDataNetworkType;
            int batteryCapacity;
            unsigned int batteryState;
            char batteryDetailString[150];
            int bluetoothBatteryCapacity;
            int thermalColor;
            unsigned int thermalSunlightMode;
            unsigned int slowActivity;
            unsigned int syncActivity;
            char activityDisplayId[256];
            unsigned int bluetoothConnected;
            unsigned int displayRawGSMSignal;
            unsigned int displayRawWiFiSignal;
            unsigned int locationIconType;
            unsigned int voiceControlIconType;
            unsigned int quietModeInactive;
            unsigned int tetheringConnectionCount;
            unsigned int batterySaverModeActive;
            unsigned int deviceIsRTL;
            unsigned int lock;
            char breadcrumbTitle[256];
            char breadcrumbSecondaryTitle[256];
            char personName[100];
            unsigned int electronicTollCollectionAvailable;
            unsigned int radarAvailable;
            unsigned int WiFiLinkWarning;
            unsigned int WiFiSearching;
            double backgroundActivityDisplayStartDate;
            unsigned int shouldShowEmergencyOnlyStatus;
            unsigned int secondaryCellularConfigured;
            char primaryServiceBadgeString[100];
            char secondaryServiceBadgeString[100];
            char quietModeImage[256];
            unsigned int extra1;
        } values;
    };
    """
# End of StatusBarOverrideData struct
    
class Setter:
    def __init__(self, workspace: str):
        self.ws = workspace

    def apply_changes(self, overrides: StatusBarOverrideData):
        path = os.join(self.ws, FileLocation.status_bar.value)
        try:
            with open(path, "wb") as out_file:
                packed = overrides.pack()
                out_file.write(packed)
                for _ in range(256):
                    out_file.write(b'\0')
        except IOError:
            print(f"Failed to open file: {path}")

    def get_overrides(self) -> StatusBarOverrideData:
        path = os.path.join(self.ws, FileLocation.status_bar.value)
        overrides = StatusBarOverrideData()
        if os.path.exists(path):
            # read and map the file
            try:
                with open(path, "rb") as in_file:
                    contents = in_file.read()
                    if contents != None:
                        overrides.unpack_from(contents)
            except IOError:
                print(f"Failed to open file: {path}")
        return overrides