import psutil

def is_running(process_name):
    process_name = process_name.lower()

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name and name.lower() == process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return False


def kill(process_name):
    process_name = process_name.lower()

    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name and name.lower() == process_name:
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue