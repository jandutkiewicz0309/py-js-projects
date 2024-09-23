import psutil

def get_memory_data():
    virtual_memory = psutil.virtual_memory()
    memory_info = {
        "total": f"{virtual_memory.total / (1024 ** 3):.2f} GB",
        "used": f"{virtual_memory.used / (1024 ** 3):.2f} GB",
        "free": f"{virtual_memory.free / (1024 ** 3):.2f} GB",
        "percent": f"{virtual_memory.percent} %"
    }
    return memory_info
