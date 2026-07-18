import wmi
import psutil

_wmi = wmi.WMI()

def get_cpu_name():
    cpu = _wmi.Win32_Processor()[0]
    return cpu.Name.strip()

def get_gpu_name():
    gpu = _wmi.Win32_VideoController()[0]
    return gpu.Name.strip()

def get_gpu_names():
    ignored_adapters = [
        "Meta Virtual Monitor",
        "Microsoft Basic Display Adapter",
    ]
    
    gpu_names = []

    for gpu in _wmi.Win32_VideoController():
        name = gpu.Name.strip()
        
        if name not in ignored_adapters:
            gpu_names.append(name)

    return gpu_names

def get_ram_modules():
    modules = []

    for stick in _wmi.Win32_PhysicalMemory():
        modules.append({
            "manufacturer": str(stick.Manufacturer).strip(),
            "capacity": round(int(stick.Capacity) / (1024**3)),
            "speed_mhz": int(stick.Speed) if stick.Speed else None,
            "configured_speed_MHz": (
                int(stick.ConfiguredClockSpeed) 
                if stick.ConfiguredClockSpeed else None
                ),
            "part_number": str(stick.PartNumber).strip(),
        })
    return modules

def get_ram_speed():
    return get_ram_modules()[0]['configured_speed_MHz']

def get_ram_base_speed():
    return get_ram_modules()[0]['speed_mhz']

def is_xmp_expo_enabled():
    if get_ram_speed() > get_ram_base_speed():
        return True
    else:
        return False

def get_board_name():
    board = _wmi.Win32_BaseBoard()[0]
    return f"{board.Manufacturer} {board.Product}"

def get_bios_version():
    bios = _wmi.Win32_BIOS()[0]
    return bios.SMBIOSBIOSVersion

def get_os_name():
    os_info = _wmi.Win32_OperatingSystem()[0]
    return os_info.Caption.strip()

def get_storage_names():
    drives = []

    for drive in _wmi.Win32_DiskDrive():
        drives.append(drive.Model)

    return drives

def get_memory():
    return psutil.virtual_memory()

def get_disk():
    return psutil.disk_usage("C:\\")

def get_total_ram():
    return round(get_memory().total / (1024**3))

def get_available_ram():
    return round(get_memory().available / (1024**3))

def get_ram_usage():
    return get_memory().percent

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_total_disk_space():
    return round(get_disk().total / (1024**3))

def get_free_disk_space():
    return round(get_disk().free / (1024**3))

def get_used_disk_space():
    return round(get_disk().used / (1024**3))