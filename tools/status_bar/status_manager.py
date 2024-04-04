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