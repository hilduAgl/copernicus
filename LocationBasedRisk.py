import numpy as np

# Example function to calculate the risk score for each location point
def calculate_risk(fishing_pressure, stock_health, historical_depletion, w1=0.4, w2=0.3, w3=0.3):
    return (w1 * fishing_pressure + w2 * (1 - stock_health) + w3 * historical_depletion)

# Example data: Coordinates, Fishing Pressure, Stock Health, Historical Depletion
coordinates = [(lat, lon) for lat in range(10, 15) for lon in range(30, 35)]
fishing_pressure_data = np.random.rand(len(coordinates))  # Random data for example
stock_health_data = np.random.rand(len(coordinates))  # Random data for example
historical_depletion_data = np.random.rand(len(coordinates))  # Random data for example

# Calculate risk scores for each location
risk_scores = []
for i, (lat, lon) in enumerate(coordinates):
    risk = calculate_risk(fishing_pressure_data[i], stock_health_data[i], historical_depletion_data[i])
    risk_scores.append((lat, lon, risk))

# Print out results for each location
for lat, lon, risk in risk_scores:
    print(f"Location ({lat}, {lon}) - Risk Score: {risk:.2f}")
