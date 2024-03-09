import hashlib
import random
import datetime

import os
import plistlib
from pathlib import Path
from shutil import copyfile, rmtree

def remove_domain(domain: str, input_str: str):
    pos = input_str.find(domain)
    if pos != -1:
        pos += len(domain)
        if pos < len(input_str) and (input_str[pos] == '\\' or input_str[pos] == '/'):
            pos += 1
        return input_str[pos:]
    return input_str

def write_str_with_len(out_file, to_write: str):
    byte_array = to_write.encode('utf-8')
    length = len(byte_array)
    big_endian_length = length.to_bytes(2, byteorder='big')

    out_file.write(big_endian_length)
    out_file.write(byte_array)

def write_hash(out_file, file):
    try:
        with open(file, "rb") as in_file:
            contents = in_file.read()
            hash_value = hashlib.sha1(contents).digest()
            out_file.write(hash_value)
    except IOError:
        print(f"Failed to open file: {file}") # TODO: Add QDebug equivalent
        return

def generate_random_hex(out_file):
    random.seed(datetime.datetime.now().timestamp())

    buffer_data = bytes([random.randint(0, 255) for _ in range(12)])
    out_file.write(buffer_data)

def calculate_sha1(data):
    return hashlib.sha1(data.encode()).hexdigest()

def process_files(path: str, domain_str: str, output_dir: Path):
    if '.DS_Store' in str(path):
        return
    file_str = remove_domain(str(domain_str), str(path)).replace('hiddendot', '.').replace('\\', '/')
    try:
        with open(output_dir.joinpath("Manifest.mbdb"), 'ab') as out_file:
            # Write the domain name string to Manifest.mbdb
            domain_name = domain_str
            if domain_str == 'ConfigProfileDomain':
                domain_name = "SysSharedContainerDomain-systemgroup.com.apple.configurationprofiles"
            write_str_with_len(out_file, domain_name)

            # Write the path string
            write_str_with_len(out_file, file_str)
            if os.path.isfile(path):
                # Path is a file
                out_file.write(b'\xFF\xFF\x00\x14')

                # Write file hash to Manifest.mbdb
                write_hash(out_file, path)
                out_file.write(b'\xFF\xFF\x81\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xF5\x00\x00\x01\xF5')
                generate_random_hex(out_file)
                # Write file size (as big endian)
                out_file.write(os.path.getsize(path).to_bytes(8, byteorder='big'))
                out_file.write(b'\x04\x00')

                # Write domain-path hash
                path_hash = calculate_sha1(f"{domain_name}-{file_str}")
                copyfile(path, output_dir.joinpath(path_hash))
            elif os.path.isdir(path):
                # Path is a directory
                out_file.write(b'\xFF\xFF\xFF\xFF\xFF\xFF\x41\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xF5\x00\x00\x01\xF5')
                generate_random_hex(out_file)
                out_file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00')

                # Recursively add the files from inside the directory
                for entry in os.listdir(path):
                    file_path = os.path.join(path, entry)
                    if not file_path.startswith('.'):
                        process_files(file_path, domain_str, output_dir)
    except IOError:
        print("Failed to create output file") # TODO: Add QDebug equivalent
        return

def create_backup(src: Path, dst: Path) -> bool:
    # Prepare
    rmtree(path=dst, ignore_errors=True)
    dst.mkdir(parents=True, exist_ok=True)

    # NOTE: Manifest.mbdb tracks the locations and SHA1 hashes of each file in the backup
    try:
        with open(dst.joinpath("Manifest.mbdb"), 'wb') as out_file:
            # Create Manifest.mbdb file header
            header = b"mbdb\x05\x00"
            out_file.write(header)
    except IOError:
        print("Failed to create output file") # TODO: Add QDebug equivalent
        return False
        
    # Iterate over all domains
    for domain in os.listdir(src):
        domain_path = os.path.join(str(src), domain)
        if os.path.isdir(domain_path) and not domain.startswith('.'):
            domain_str = os.path.basename(domain_path)
            process_files(domain_path, domain_str, dst)

    # Generate Info.plist
    info_plist_content = b"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
</dict>
</plist>"""
    try:
        with open(dst.joinpath("Info.plist"), 'wb') as info_plist:
            info_plist.write(info_plist_content)
    except IOError:
        print("Failed to create Info.plist file") # TODO: Add QDebug equivalent
        return False
    
    # Generate Status.plist
    status_plist_content = b"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>BackupState</key>
	<string>new</string>
	<key>Date</key>
	<date>1970-01-01T00:00:00Z</date>
	<key>IsFullBackup</key>
	<false/>
	<key>SnapshotState</key>
	<string>finished</string>
	<key>UUID</key>
	<string>00000000-0000-0000-0000-000000000000</string>
	<key>Version</key>
	<string>2.4</string>
</dict>
</plist>"""
    try:
        with open(dst.joinpath("Status.plist"), 'wb') as status_plist:
            status_plist.write(status_plist_content)
    except IOError:
        print("Failed to create Status.plist file") # TODO: Add QDebug equivalent
        return False
    
    # Generate Manifest.plist
    manifest_plist_content = b"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>BackupKeyBag</key>
	<data>
    VkVSUwAAAAQAAAAFVFlQRQAAAAQAAAABVVVJRAAAABDud41d1b9NBICR1BH9JfVtSE1D
    SwAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAV1JBUAAA
    AAQAAAAAU0FMVAAAABRY5Ne2bthGQ5rf4O3gikep1e6tZUlURVIAAAAEAAAnEFVVSUQA
    AAAQB7R8awiGR9aba1UuVahGPENMQVMAAAAEAAAAAVdSQVAAAAAEAAAAAktUWVAAAAAE
    AAAAAFdQS1kAAAAoN3kQAJloFg+ukEUY+v5P+dhc/Welw/oucsyS40UBh67ZHef5ZMk9
    UVVVSUQAAAAQgd0cg0hSTgaxR3PVUbcEkUNMQVMAAAAEAAAAAldSQVAAAAAEAAAAAktU
    WVAAAAAEAAAAAFdQS1kAAAAoMiQTXx0SJlyrGJzdKZQ+SfL124w+2Tf/3d1R2i9yNj9z
    ZCHNJhnorVVVSUQAAAAQf7JFQiBOS12JDD7qwKNTSkNMQVMAAAAEAAAAA1dSQVAAAAAE
    AAAAAktUWVAAAAAEAAAAAFdQS1kAAAAoSEelorROJA46ZUdwDHhMKiRguQyqHukotrxh
    jIfqiZ5ESBXX9txi51VVSUQAAAAQfF0G/837QLq01xH9+66vx0NMQVMAAAAEAAAABFdS
    QVAAAAAEAAAAAktUWVAAAAAEAAAAAFdQS1kAAAAol0BvFhd5bu4Hr75XqzNf4g0fMqZA
    ie6OxI+x/pgm6Y95XW17N+ZIDVVVSUQAAAAQimkT2dp1QeadMu1KhJKNTUNMQVMAAAAE
    AAAABVdSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAo2N2DZarQ6GPoWRgTiy/t
    djKArOqTaH0tPSG9KLbIjGTOcLodhx23xFVVSUQAAAAQQV37JVZHQFiKpoNiGmT6+ENM
    QVMAAAAEAAAABldSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAofe2QSvDC2cV7
    Etk4fSBbgqDx5ne/z1VHwmJ6NdVrTyWi80Sy869DM1VVSUQAAAAQFzkdH+VgSOmTj3yE
    cfWmMUNMQVMAAAAEAAAAB1dSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAo7kLY
    PQ/DnHBERGpaz37eyntIX/XzovsS0mpHW3SoHvrb9RBgOB+WblVVSUQAAAAQEBpgKOz9
    Tni8F9kmSXd0sENMQVMAAAAEAAAACFdSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kA
    AAAo5mxVoyNFgPMzphYhm1VG8Fhsin/xX+r6mCd9gByF5SxeolAIT/ICF1VVSUQAAAAQ
    rfKB2uPSQtWh82yx6w4BoUNMQVMAAAAEAAAACVdSQVAAAAAEAAAAA0tUWVAAAAAEAAAA
    AFdQS1kAAAAo5iayZBwcRa1c1MMx7vh6lOYux3oDI/bdxFCW1WHCQR/Ub1MOv+QaYFVV
    SUQAAAAQiLXvK3qvQza/mea5inss/0NMQVMAAAAEAAAACldSQVAAAAAEAAAAA0tUWVAA
    AAAEAAAAAFdQS1kAAAAoD2wHX7KriEe1E31z7SQ7/+AVymcpARMYnQgegtZD0Mq2U55u
    xwNr2FVVSUQAAAAQ/Q9feZxLS++qSe/a4emRRENMQVMAAAAEAAAAC1dSQVAAAAAEAAAA
    A0tUWVAAAAAEAAAAAFdQS1kAAAAocYda2jyYzzSKggRPw/qgh6QPESlkZedgDUKpTr4Z
    Z8FDgd7YoALY1g==
    </data>
	<key>Lockdown</key>
	<dict/>
	<key>SystemDomainsVersion</key>
	<string>20.0</string>
	<key>Version</key>
	<string>9.1</string>
</dict>
</plist>"""
    try:
        with open(dst.joinpath("Manifest.plist"), 'wb') as manifest_plist:
            manifest_plist.write(manifest_plist_content)
    except IOError:
        print("Failed to create Manifest.plist file") # TODO: Add QDebug equivalent
        return False
    
    return True