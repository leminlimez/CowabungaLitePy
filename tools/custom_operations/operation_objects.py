import uuid

## Main Operation Object
class AdvancedObject:
    def __init__(self,
                name: str, filePath: str, author: str = "", version: str = "1.0",
                icon: str = None, locked: bool = False,
                hasPrefs: bool = False, enabled: bool = False):
        """
        Create an AdvancedObject instance

        :param name: Operation name
        :param author: Operation author
        :param version: Operation version
        :param icon: Operation icon file path (optional)
        :param locked: If it has been exported, so that user cannot change certain properties like author and version
        :param hasPrefs: If it has preferences/certain properties or files that the user can modify, even when locked (loads separately)
        :param enabled: If the tweak is enabled
        """
        self.id = uuid.uuid4
        self.name = name
        self.filePath = filePath
        self.author = author
        self.version = version
        self.icon = icon
        self.locked = locked
        self.hasPrefs = hasPrefs
        self.enabled = enabled

    def set_enabled(self, enabled: bool):
        self.enabled = enabled