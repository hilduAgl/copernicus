class FishingPressure:
    def __init__(self, total_catch, num_vessels):
        self.total_catch = total_catch
        self.num_vessels = num_vessels

    def calculate_pressure(self):
        if self.num_vessels == 0:  # Prevent division by zero
            return 0
        return self.total_catch / self.num_vessels
class FishingPressure:
    def __init__(self, total_catch, num_vessels):
        self.total_catch = total_catch
        self.num_vessels = num_vessels

    def calculate_pressure(self):
        if self.num_vessels == 0:  # Prevent division by zero
            return 0
        return self.total_catch / self.num_vessels
