import plistlib

def get_plist_value(file: str, key: str):
    with open(file, 'rb') as in_fp:
        plist = plistlib.load(in_fp)
    return plist[key] if key in plist else None

def set_plist_value(file: str, key: str, value):
    with open(file, 'rb') as in_fp:
        plist = plistlib.load(in_fp)
    plist[key] = value
    with open(file, 'wb') as out_fp:
        plistlib.dump(plist, out_fp)

def delete_plist_key(file: str, key: str):
    with open(file, 'rb') as in_fp:
        plist = plistlib.load(in_fp)
    del plist[key]
    with open(file, 'wb') as out_fp:
        plistlib.dump(plist, out_fp)