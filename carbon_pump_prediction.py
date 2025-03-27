import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Title of the app
st.title("Biological Carbon Pump Prediction")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")
phytoplankton = st.sidebar.slider("Phytoplankton Productivity (Chlorophyll-a)", 0.0, 20.0, 10.0)
sinking_speed = st.sidebar.slider("Sinking Speed of Marine Snow (m/day)", 0.1, 2.0, 1.0)
ocean_temperature = st.sidebar.slider("Ocean Temperature (°C)", -2.0, 30.0, 10.0)
acidification = st.sidebar.slider("Ocean Acidification (pH)", 7.5, 8.5, 8.0)

# Dummy model to simulate predictions (for demo)
def predict_sequestration(phytoplankton, sinking_speed, ocean_temperature, acidification):
    # Example coefficients for a simple linear regression model
    coefficients = np.array([0.05, 0.3, -0.02, -0.1])
    inputs = np.array([phytoplankton, sinking_speed, ocean_temperature, acidification])
    return np.dot(coefficients, inputs)  # Linear combination of inputs

# Display the inputs
st.write(f"Phytoplankton Productivity: {phytoplankton} µg/L")
st.write(f"Sinking Speed: {sinking_speed} m/day")
st.write(f"Ocean Temperature: {ocean_temperature} °C")
st.write(f"Ocean Acidification: {acidification} pH")

# Prediction
prediction = predict_sequestration(phytoplankton, sinking_speed, ocean_temperature, acidification)
st.write(f"Predicted Biological Carbon Pump Efficiency: {prediction:.2f} (Relative Units)")

# Visualizing data (for demo)
x = np.linspace(0, 20, 100)
y = 0.05 * x + 0.3 * np.ones(100) + 0.02 * np.random.randn(100)

fig, ax = plt.subplots()
ax.scatter(x, y, color='blue')
ax.set_xlabel("Phytoplankton Productivity")
ax.set_ylabel("Carbon Sequestration Efficiency")
ax.set_title("Carbon Sequestration Prediction Visualization")
st.pyplot(fig)
