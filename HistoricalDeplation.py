class HistoricalDepletion:
    def __init__(self, historical_catch, historical_stock):
        self.historical_catch = historical_catch
        self.historical_stock = historical_stock

    def calculate_depletion(self):
        if self.historical_stock == 0:  # Avoid division by zero
            return 0
        depletion = self.historical_catch / self.historical_stock
        return min(1, depletion)  # Ensure depletion value doesn't exceed 1
