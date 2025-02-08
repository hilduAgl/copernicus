class StockHealth:
    def __init__(self, chlorophyll_a, sea_surface_temp):
        self.chlorophyll_a = chlorophyll_a
        self.sea_surface_temp = sea_surface_temp

    def calculate_health(self):
        # For simplicity, assume chlorophyll_a and SST are in ideal ranges
        # This can be adjusted to more complex logic based on expert data
        if self.chlorophyll_a < 0.2:  # Low chlorophyll is bad for fish
            health = 0.2
        elif self.chlorophyll_a > 0.8:  # High chlorophyll is good for fish
            health = 0.8
        else:
            health = 0.5
        
        if self.sea_surface_temp > 28:  # High SST may be harmful for many species
            health -= 0.1

        return max(0, min(1, health))  # Ensure value stays between 0 and 1
