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
