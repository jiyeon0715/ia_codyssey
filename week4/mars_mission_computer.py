import time
import json

class DummySensor:
    def get_internal_temperature(self):
        return 21.5

    def get_external_temperature(self):
        return -63.0

    def get_internal_humidity(self):
        return 45.0

    def get_external_illuminance(self):
        return 12000.0

    def get_internal_co2(self):
        return 600.0

    def get_internal_oxygen(self):
        return 19.5


class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0.0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }
        self.ds = DummySensor()
        self.history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

    def get_sensor_data(self):
        start_time = time.time()
        while True:
            self.env_values['mars_base_internal_temperature'] = self.ds.get_internal_temperature()
            self.env_values['mars_base_external_temperature'] = self.ds.get_external_temperature()
            self.env_values['mars_base_internal_humidity'] = self.ds.get_internal_humidity()
            self.env_values['mars_base_external_illuminance'] = self.ds.get_external_illuminance()
            self.env_values['mars_base_internal_co2'] = self.ds.get_internal_co2()
            self.env_values['mars_base_internal_oxygen'] = self.ds.get_internal_oxygen()

            for key in self.env_values:
                self.history[key].append(self.env_values[key])

            print(json.dumps(self.env_values, indent=4))

            if int(time.time() - start_time) % 300 == 0:
                print('--- 5 minute average values ---')
                for key in self.history:
                    values = self.history[key][-60:]  # 마지막 5분 (5초 간격 x 60회)
                    if values:
                        avg = sum(values) / len(values)
                        print(f'{key}: {avg:.2f}')
                print('-------------------------------')

            print('Press Ctrl+C to stop...\n')
            try:
                time.sleep(5)
            except KeyboardInterrupt:
                print('System stopped…')
                break


RunComputer = MissionComputer()
RunComputer.get_sensor_data()
