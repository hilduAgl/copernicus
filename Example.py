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

class OverfishingRisk:
    def __init__(self, fishing_pressure, stock_health, historical_depletion, w1=0.4, w2=0.3, w3=0.3):
        self.fishing_pressure = fishing_pressure
        self.stock_health = stock_health
        self.historical_depletion = historical_depletion
        self.w1 = w1  # Weight for fishing pressure
        self.w2 = w2  # Weight for stock health
        self.w3 = w3  # Weight for historical depletion

    def calculate_risk(self):
        return (self.w1 * self.fishing_pressure +
                self.w2 * (1 - self.stock_health) +  # Inverse of stock health
                self.w3 * self.historical_depletion)

    def categorize_risk(self, risk_score):
        if risk_score < 0.4:
            return "Low"
        elif risk_score < 0.7:
            return "Medium"
        else:
            return "High"

class HistoricalDepletion:
    def __init__(self, historical_catch, historical_stock):
        self.historical_catch = historical_catch
        self.historical_stock = historical_stock

    def calculate_depletion(self):
        if self.historical_stock == 0:  # Avoid division by zero
            return 0
        depletion = self.historical_catch / self.historical_stock
        return min(1, depletion)  # Ensure depletion value doesn't exceed 1

# Example data
total_catch = 500  # tons
num_vessels = 50
chlorophyll_a = 0.5  # Range: 0-1 (ideal is 0.3-0.7)
sea_surface_temp = 26  # Celsius
historical_catch = 2000  # tons
historical_stock = 5000  # tons

# Instantiate classes
fishing_pressure = FishingPressure(total_catch, num_vessels)
stock_health = StockHealth(chlorophyll_a, sea_surface_temp)
historical_depletion = HistoricalDepletion(historical_catch, historical_stock)

# Calculate individual factors
fishing_pressure_value = fishing_pressure.calculate_pressure()
stock_health_value = stock_health.calculate_health()
historical_depletion_value = historical_depletion.calculate_depletion()

# Calculate overfishing risk
risk_model = OverfishingRisk(fishing_pressure_value, stock_health_value, historical_depletion_value)
risk_score = risk_model.calculate_risk()
risk_category = risk_model.categorize_risk(risk_score)

print(f"Risk Score: {risk_score:.2f}")
print(f"Risk Category: {risk_category}")
