def hex_to_little_endian(hex_str):
    byte_str = bytes.fromhex(hex_str)
    little_endian = byte_str[::-1].hex()
    return little_endian

def hex_to_binary(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def calculate_partition_size(sectors, sector_size=512):
    bytes_size = sectors * sector_size
    kb_size = bytes_size / 1024
    mb_size = kb_size / 1024
    return bytes_size, kb_size, mb_size

def get_partition_type_label(partition_type_hex):
    partition_labels = {
        "00": "Should NOT be used in an actual table entry!",
        "01": "12-bit FAT",
        "02": "XENIX root",
        "03": "XENIX /usr (obsolete)",
        "04": "16-bit FAT, partition; of sizes less than 32 MB.",
        "05": "Extended Partition; within the first 1024 cylinders of a disk drive",
        "06": "16-bit FAT, partition; greater than or equal to 32 MB.",
        "07": "Installable file systems: HPFS or NTFS. Also, QNX and Advanced Unix.",
        "08": "AIX bootable partition, AIX (Linux), SplitDrive, OS/2",
        "09": "AIX data partition, AIX bootable (Linux), Coherent file system, QNX.",
        "0A": "Coherent swap partition, OPUS or OS/2 Boot Manager.",
        "0B": "32-bit FAT",
        "0C": "32-bit FAT, using INT 13 Extensions.",
        "0E": "16-bit FAT >= 32 MB, using INT 13 Extensions.",
        "0F": "Extended Partition, using INT 13 Extensions",
        "11": "Hidden 12-bit FAT.",
        "12": "Compaq diagnostics.",
        "14": "Hidden 16-bit FAT, partition <32 MB",
        "16": "Hidden 16-bit FAT, partition >= 32 MB",
        "17": "Hidden IFS (HPFS, NTFS).",
        "18": "AST Windows swap file",
        "19": "Willowtech Photon coS",
        "1B": "Hidden 32-bit FAT",
        "1C": "Hidden 32-bit FAT, Ext INT 13",
        "1E": "Hidden 16-bit FAT >32 MB, Ext. INT 13 (PowerQuest specific)",
        "20": "Willowsoft Overture File System (OFS1)",
        "21": "reserved (HP Volume Expansion, SpeedStor variant)",
        "22": "Oxygen Extended",
        "23": "reserved (HP Volume Expansion, SpeedStor variant?)",
        "24": "NEC MS-DOS 3.x",
        "26": "reserved (HP Volume Expansion, SpeedStor variant?)",
        "31": "reserved (HP Volume Expansion, SpeedStor variant?)",
        "33": "reserved (HP Volume Expansion, SpeedStor variant?)",
        "34": "reserved (HP Volume Expansion, SpeedStor variant?)",
        "36": "reserved (HP Volume Expansion, SpeedStor variant?)",
        "38": "Theos",
        "3C": "PowerQuest Files Partition Format",
        "3D": "Hidden NetWare",
        "40": "VENIX 80286",
        "41": "Personal RISC Boot, PowerPC boot partition",
        "42": "Secure File System, Windows 2000/XP (NT 5): Dynamic extended partition",
        "43": "Alternative Linux native file system (EXT2fs)",
        "45": "Priam, EUMEL/Elan.",
        "46": "EUMEL/Elan",
        "47": "EUMEL/Elan",
        "48": "EUMEL/Elan",
        "4A": "ALFS/THIN lightweight filesystem for DOS",
        "4D": "QNX",
        "4E": "QNX",
        "4F": "QNX, Oberon boot/data partition.",
        "50": "Ontrack Disk Manager, read-only partition, FAT partition (Logical sector size varies)",
        "51": "Ontrack Disk Manager, read/write partition, FAT partition (Logical sector size varies)",
        "52": "CP/M, Microport System V/386.",
        "53": "Ontrack Disk Manager, write-only",
        "54": "Ontrack Disk Manager 6.0 (DDO)",
        "55": "EZ-Drive 3.05",
        "56": "Golden Bow VFeature",
        "5C": "Priam EDISK",
        "61": "Storage Dimensions SpeedStor",
        "63": "GNU HURD, Mach, MtXinu BSD 4.2 on Mach, Unix Sys V/386, 386/ix.",
        "64": "Novell NetWare 286, SpeedStore.",
        "65": "Novell NetWare (3.11 and 4.1)",
        "66": "Novell NetWare 386",
        "67": "Novell NetWare",
        "68": "Novell NetWare",
        "69": "Novell NetWare 5+; Novell Storage Services (NSS)",
        "70": "DiskSecure Multi-Boot",
        "75": "IBM PC/IX",
        "80": "Minix v1.1 - 1.4a, Old MINIX (Linux).",
        "81": "Linux/Minix v1.4b+, Mitac Advanced Disk Manager.",
        "82": "Linux Swap partition, Prime or Solaris (Unix).",
        "83": "Linux native file systems (ext2/3/4, JFS, Reiser, xiafs, and others).",
        "84": "OS/2 hiding type 04h partition",
        "86": "NT Stripe Set, Volume Set?",
        "87": "NT Stripe Set, Volume Set?, HPFS FT mirrored partition.",
        "93": "Amoeba file system, Hidden Linux EXT2 partition (PowerQuest).",
        "94": "Amoeba bad block table",
        "99": "Mylex EISA SCSI",
        "9F": "BSDI",
        "A0": "Phoenix NoteBios Power Management 'Save to Disk', IBM hibernation.",
        "A1": "HP Volume Expansion (SpeedStor variant)",
        "A3": "HP Volume Expansion (SpeedStor variant)",
        "A4": "HP Volume Expansion (SpeedStor variant)",
        "A5": "FreeBSD/386",
        "A6": "OpenBSD",
        "A7": "NextStep Partition",
        "A9": "NetBSD",
        "AA": "Olivetti DOS with FAT12",
        "B0": "Bootmanager BootStar by Star-Tools GmbH",
        "B1": "HP Volume Expansion (SpeedStor variant)",
        "B3": "HP Volume Expansion (SpeedStor variant)",
        "B4": "HP Volume Expansion (SpeedStor variant)",
        "B6": "HP Volume Expansion (SpeedStor variant)",
        "B7": "BSDI file system or secondarily swap",
        "B8": "BSDI swap partition or secondarily file system",
        "BB": "PTS BootWizard (hidden) 4.0; but now also used by Acronis OS Selector",
        "BC": "May be an Acronis 'Backup' or 'Secure Zone' partition",
        "BE": "Solaris boot partition",
        "C0": "Novell DOS/OpenDOS/DR-OpenDOS/DR-DOS secured partition",
        "C1": "DR-DOS 6.0 LOGIN.EXE-secured 12-bit FAT partition",
        "C4": "DR-DOS 6.0 LOGIN.EXE-secured 16-bit FAT partition",
        "C6": "DR-DOS 6.0 LOGIN.EXE-secured Huge partition",
        "C7": "Syrinx, Cyrnix, HPFS FT disabled mirrored partition",
        "D0": "Multiuser DOS secured (FAT12???)",
        "DB": "CP/M, Concurrent CP/M, Concurrent DOS, or CTOS",
        "DE": "Dell partition",
        "DF": "BootIt EMBRM",
        "E1": "SpeedStor 12-bit FAT Extended partition, DOS access (Linux).",
        "EB": "BeOS file system",
        "EE": "Indicates a GPT Protective MBR followed by a GPT/EFI Header.",
        "EF": "EFI/UEFI System Partition (or ESP)",
        "FD": "Reserved for FreeDOS",
        "FF": "Xenix bad-block table"
    }
    return partition_labels.get(partition_type_hex, "Unknown Partition Type")

def parse_partition_data(data):
    bootable_flag = data[0:2]
    start_chs_hex = data[2:8]
    partition_type_hex = data[8:10]
    end_chs_hex = data[10:16]
    lba_hex = data[16:24]
    num_sectors_hex = data[24:32]

    start_chs_little = hex_to_little_endian(start_chs_hex)
    start_chs_binary = hex_to_binary(start_chs_little)
    head_start = binary_to_decimal(start_chs_binary[0:8])
    sector_start = binary_to_decimal(start_chs_binary[8:14])
    cylinder_start = binary_to_decimal(start_chs_binary[14:24])

    end_chs_little = hex_to_little_endian(end_chs_hex)
    end_chs_binary = hex_to_binary(end_chs_little)
    head_end = binary_to_decimal(end_chs_binary[0:8])
    sector_end = binary_to_decimal(end_chs_binary[8:14])
    cylinder_end = binary_to_decimal(end_chs_binary[14:24])

    lba = int(hex_to_little_endian(lba_hex), 16)
    num_sectors = int(hex_to_little_endian(num_sectors_hex), 16)

    partition_type_label = get_partition_type_label(partition_type_hex)
    bytes_size, kb_size, mb_size = calculate_partition_size(num_sectors)

    partition_info = {
        "Bootable Flag": bootable_flag,
        "Partition Type (Hex)": partition_type_hex,
        "Partition Type (Label)": partition_type_label,
        "Start CHS": {
            "Cylinder": cylinder_start,
            "Head": head_start,
            "Sector": sector_start
        },
        "End CHS": {
            "Cylinder": cylinder_end,
            "Head": head_end,
            "Sector": sector_end
        },
        "LBA Start": lba,
        "Number of Sectors": num_sectors,
        "Size in Bytes": bytes_size,
        "Size in KB": kb_size,
        "Size in MB": mb_size
    }

    return partition_info

# Example usage
partition_data = input("Enter the partition data (32 hex characters): ").strip()
if len(partition_data) == 32:
    result = parse_partition_data(partition_data)
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print("Invalid input. Please enter exactly 32 hex characters.")

