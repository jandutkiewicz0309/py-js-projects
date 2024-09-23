import psutil

def get_disk_data():
    disk = psutil.disk_usage('/')
    
    disk_info = {
        "total": f"{disk.total / (1024 ** 4): .2f} TB",
        "used": f"{disk.used / (1024 ** 4): .2f} TB",
        "free": f"{disk.free / (1024 ** 3): .2f} TB",
        "percent": f"{disk.percent}%"
    }
    return disk_info
