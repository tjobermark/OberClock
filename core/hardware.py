import psutil

def get_memory():
    return psutil.virtual_memory()

def get_disk():
    return psutil.disk_usage("/")

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