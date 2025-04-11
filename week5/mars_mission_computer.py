import platform
import os
import json
import psutil


class MissionComputer:
    def __init__(self):
        self.env_values = {}

    def get_mission_computer_info(self):
        try:
            info = {
                'os': platform.system(),
                'os_version': platform.version(),
                'cpu_type': platform.processor(),
                'cpu_core_count': os.cpu_count(),
                'memory_size': f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
            }
            print(json.dumps(info, indent=4))
            return info
        except Exception as e:
            print(f'Error retrieving system info: {e}')
            return {}

    def get_mission_computer_load(self):
        try:
            load = {
                'cpu_usage_percent': psutil.cpu_percent(interval=1),
                'memory_usage_percent': psutil.virtual_memory().percent
            }
            print(json.dumps(load, indent=4))
            return load
        except Exception as e:
            print(f'Error retrieving system load: {e}')
            return {}


if __name__ == '__main__':
    runComputer = MissionComputer()
    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
