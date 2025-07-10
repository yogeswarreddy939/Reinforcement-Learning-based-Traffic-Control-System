import random

class TrafficEnvironment:
    def __init__(self):
        self.state = 0  # 0 = low congestion, 1 = medium, 2 = high

    def get_state(self, vehicle_count):
        if vehicle_count < 5:
            return 0
        elif vehicle_count < 15:
            return 1
        else:
            return 2

    def get_reward(self, state, action):
        # action: 0 = short green, 1 = long green
        if state == 2 and action == 1:
            return 10  # long green when congestion is high
        elif state == 0 and action == 0:
            return 8   # short green when traffic is light
        else:
            return -5  # bad decision

