import os
from pathlib import Path

from pymobiledevice3.services.mobile_image_mounter import DeveloperDiskImageMounter, MobileImageMounterService, \
    PersonalizedImageMounter, auto_mount
from pymobiledevice3.exceptions import AlreadyMountedError, DeveloperDiskImageNotFoundError, NotMountedError, \
    UnsupportedCommandError
from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.lockdown_service_provider import LockdownServiceProvider
from pymobiledevice3.services.dvt.instruments.location_simulation import LocationSimulation

from devicemanagement.constants import Device

def mount_dev_disk(device: Device, ld: LockdownServiceProvider) -> str:
    # create the dev disk folder
    path: Path = Path(os.path.expanduser("~/Documents")).joinpath("CowabungaLiteData").joinpath("DevDisks")
    path.mkdir(parents=True, exist_ok=True)
    try:
        auto_mount(ld, xcode=path.absolute, version=device.version)
        return 'Success'
    except DeveloperDiskImageNotFoundError:
        return 'Unable to find the correct DeveloperDiskImage'
    except AlreadyMountedError:
        return 'DeveloperDiskImage already mounted'
    except PermissionError as e:
        return (
            f'DeveloperDiskImage could not be saved to Xcode default path ({e.filename}). '
            f'Please make sure your user has the necessary permissions')
    return "???"

