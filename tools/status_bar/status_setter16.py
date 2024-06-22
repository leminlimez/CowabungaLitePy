import os
from enum import Enum
from cffi import FFI
ffi = FFI()
ffi.set_source("status_manager", "", extra_compile_args=["-mno-ms-bitfields", "-malign-double"])

from devicemanagement.constants import FileLocation

ffi.cdef("""
    typedef struct
    {
        bool itemIsEnabled[45];
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
        char serviceImages[2][100];
        char operatorDirectory[1024];
        unsigned int serviceContentType;
        unsigned int secondaryServiceContentType;
        unsigned int cellLowDataModeActive : 1;
        unsigned int secondaryCellLowDataModeActive : 1;
        int wifiSignalStrengthRaw;
        int wifiSignalStrengthBars;
        unsigned int wifiLowDataModeActive : 1;
        unsigned int dataNetworkType;
        unsigned int secondaryDataNetworkType;
        int batteryCapacity;
        unsigned int batteryState;
        char batteryDetailString[150];
        int bluetoothBatteryCapacity;
        int thermalColor;
        unsigned int thermalSunlightMode : 1;
        unsigned int slowActivity : 1;
        unsigned int syncActivity : 1;
        char activityDisplayId[256];
        unsigned int bluetoothConnected : 1;
        unsigned int displayRawGSMSignal : 1;
        unsigned int displayRawWifiSignal : 1;
        unsigned int locationIconType : 1;
        unsigned int voiceControlIconType : 2;
        unsigned int quietModeInactive : 1;
        unsigned int tetheringConnectionCount;
        unsigned int batterySaverModeActive : 1;
        unsigned int deviceIsRTL : 1;
        unsigned int lock : 1;
        char breadcrumbTitle[256];
        char breadcrumbSecondaryTitle[256];
        char personName[100];
        unsigned int electronicTollCollectionAvailable : 1;
        unsigned int radarAvailable : 1;
        unsigned int wifiLinkWarning : 1;
        unsigned int wifiSearching : 1;
        double backgroundActivityDisplayStartDate;
        unsigned int shouldShowEmergencyOnlyStatus : 1;
        unsigned int secondaryCellularConfigured : 1;
        char primaryServiceBadgeString[100];
        char secondaryServiceBadgeString[100];
        char quietModeImage[256];
        char quietModeName[256];
    } StatusBarRawData;

    typedef struct
    {
        bool overrideItemIsEnabled[45];
        unsigned int overrideTimeString : 1;
        unsigned int overrideDateString : 1;
        unsigned int overrideGSMSignalStrengthRaw : 1;
        unsigned int overrideSecondaryGSMSignalStrengthRaw : 1;
        unsigned int overrideGSMSignalStrengthBars : 1;
        unsigned int overrideSecondaryGSMSignalStrengthBars : 1;
        unsigned int overrideServiceString : 1;
        unsigned int overrideSecondaryServiceString : 1;
        unsigned int overrideServiceImages : 2;
        unsigned int overrideOperatorDirectory : 1;
        unsigned int overrideServiceContentType : 1;
        unsigned int overrideSecondaryServiceContentType : 1;
        unsigned int overrideWifiSignalStrengthRaw : 1;
        unsigned int overrideWifiSignalStrengthBars : 1;
        unsigned int overrideDataNetworkType : 1;
        unsigned int overrideSecondaryDataNetworkType : 1;
        unsigned int disallowsCellularDataNetworkTypes : 1;
        unsigned int overrideBatteryCapacity : 1;
        unsigned int overrideBatteryState : 1;
        unsigned int overrideBatteryDetailString : 1;
        unsigned int overrideBluetoothBatteryCapacity : 1;
        unsigned int overrideThermalColor : 1;
        unsigned int overrideSlowActivity : 1;
        unsigned int overrideActivityDisplayId : 1;
        unsigned int overrideBluetoothConnected : 1;
        unsigned int overrideBreadcrumb : 1;
        unsigned int overrideLock;
        unsigned int overrideDisplayRawGSMSignal : 1;
        unsigned int overrideDisplayRawWifiSignal : 1;
        unsigned int overridePersonName : 1;
        unsigned int overrideWifiLinkWarning : 1;
        unsigned int overrideSecondaryCellularConfigured : 1;
        unsigned int overridePrimaryServiceBadgeString : 1;
        unsigned int overrideSecondaryServiceBadgeString : 1;
        unsigned int overrideQuietModeImage : 1;
        unsigned int overrideQuietModeName : 1;
        StatusBarRawData values;
    } StatusBarOverrideData;
""")
    
class Setter:
    class StatusBarItem(Enum):
        TimeStatusBarItem = 0
        DateStatusBarItem = 1
        QuietModeStatusBarItem = 2
        AirplaneModeStatusBarItem = 3
        CellularSignalStrengthStatusBarItem = 4
        SecondaryCellularSignalStrengthStatusBarItem = 5
        CellularServiceStatusBarItem = 6
        SecondaryCellularServiceStatusBarItem = 7
        # 8
        CellularDataNetworkStatusBarItem = 9
        SecondaryCellularDataNetworkStatusBarItem = 10
        # 11
        MainBatteryStatusBarItem = 12
        ProminentlyShowBatteryDetailStatusBarItem = 13
        # 14
        # 15
        BluetoothStatusBarItem = 16
        TTYStatusBarItem = 17
        AlarmStatusBarItem = 18
        # 19
        # 20
        LocationStatusBarItem = 21
        RotationLockStatusBarItem = 22
        CameraUseStatusBarItem = 23
        AirPlayStatusBarItem = 24
        AssistantStatusBarItem = 25
        CarPlayStatusBarItem = 26
        StudentStatusBarItem = 27
        MicrophoneUseStatusBarItem = 28
        VPNStatusBarItem = 29
        # 30
        # 31
        # 32
        # 33
        # 34
        # 35
        # 36
        # 37
        LiquidDetectionStatusBarItem = 38
        VoiceControlStatusBarItem = 39
        # 40
        # 41
        # 42
        # 43
        Extra1StatusBarItem = 44
    
    def __init__(self, workspace: str):
        self.ws = workspace
        self.current_overrides = None

    def apply_changes(self, overrides):
        path = os.path.join(self.ws, FileLocation.status_bar.value)
        try:
            with open(path, "wb") as out_file:
                out_file.write(ffi.buffer(overrides))
            self.current_overrides = overrides
        except IOError:
            print(f"Failed to open file: {path}")

    def get_overrides(self):
        if self.current_overrides != None:
            return self.current_overrides
        path = os.path.join(self.ws, FileLocation.status_bar.value)
        overrides = ffi.new("StatusBarOverrideData *")
        if os.path.exists(path):
            # read and map the file
            try:
                with open(path, "rb") as in_file:
                    in_file.readinto(ffi.buffer(overrides))
            except IOError:
                print(f"Failed to open file: {path}")
        return overrides