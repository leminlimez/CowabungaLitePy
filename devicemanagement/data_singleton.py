from pathlib import Path

from devicemanagement.constants import Device, Tweak

class DataSingleton:
    def __init__(self):
        self.current_device: Device
        self.enabled_tweaks: list[Tweak] = []
        self.device_available: bool = False
        self.current_workspace: Path
    
    def set_tweak_enabled(self, tweak: Tweak, enabled: bool):
        if enabled:
            self.enabled_tweaks.append(tweak)
        else:
            self.enabled_tweaks.remove(tweak)
        
    def is_tweak_enabled(self, tweak: Tweak) -> bool:
        return tweak in self.enabled_tweaks