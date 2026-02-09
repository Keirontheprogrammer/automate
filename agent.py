import time
import platform
import yaml

from monitor.processes import is_running, kill
from actions.windows import open_app as open_windows
from actions.linux import open_app as open_linux

with open("config.yaml") as f:
    config = yaml.safe_load(f)

OS = platform.system()
limit = config["apps"]["distraction"]["limit_minutes"] * 60
process_name =config["apps"]["distraction"]["name"]

start_time = None
while True:
    if is_running(process_name):
        print("vlc detected")
        if start_time is None:
            start_time = time.time()
            print("Timer has started")

        elif time.time() - start_time >= limit:
            kill(process_name)

            if OS =="Windows":
                for app in config["apps"]["reward"]["windows"]:
                    open_windows(app)

            else: 
                for app in config["apps"]["reward"]["linux"]:
                    open_linux(app)

            start_time = None

    else:
        start_time = None

    print("Agent is running")
    
    time.sleep(config["check_interval_seconds"])