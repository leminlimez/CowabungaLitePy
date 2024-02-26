from enum import Enum

class Device:
    def __init__(self, uuid: int, name: str, version: str, ipad: bool):
        self.uuid = uuid
        self.name = name
        self.version = version
        self.ipad = ipad
    
class Tweak(Enum):
    springboard_options = 'SpringboardOptions'