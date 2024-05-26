import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set style for Seaborn
sns.set(style="whitegrid")

# Title
st.title("BIM4Energy Case Study Explorer")

# Input selections
st.sidebar.header("Select Case Study Parameters")

# Building types
building_types = ["Dormitory", "Office", "Hotel", "Hospital", "School"]
building_type = st.sidebar.selectbox("Select building type", building_types)

# European cities (climate scenarios)
cities = ["Vilnius", "Berlin", "Paris", "Madrid", "Rome"]
climate_scenario = st.sidebar.selectbox("Select climate scenario", cities)

# Building archetype
archetypes = ["Residential", "Commercial", "Industrial", "Public"]
archetype = st.sidebar.selectbox("Select archetype", archetypes)

# Orientation of the main facade
orientations = ["North", "South", "East", "West"]
orientation = st.sidebar.selectbox("Select orientation of main facade", orientations)

# Energy efficiency strategies
st.sidebar.header("Energy Efficiency Strategies")
thermal_envelope = st.sidebar.slider("Thermal envelope improvement (%)", 0, 100, 50)
heating_system = st.sidebar.slider("Heating system efficiency (%)", 0, 100, 50)
ventilation_system = st.sidebar.slider("Ventilation system efficiency (%)", 0, 100, 50)
renewable_energy = st.sidebar.slider("Renewable energy supply (%)", 0, 100, 50)
building_operation = st.sidebar.slider("Improved building operation (%)", 0, 100, 50)

# Base energy consumption data (dummy data)
base_energy_data = {
    "Heating": 100,
    "Cooling": 50,
    "Other": 30
}

# Calculate improved energy consumption based on selected strategies
improved_energy_data = {
    "Heating": base_energy_data["Heating"] * (1 - heating_system / 100) * (1 - thermal_envelope / 100),
    "Cooling": base_energy_data["Cooling"] * (1 - ventilation_system / 100) * (1 - thermal_envelope / 100),
    "Other": base_energy_data["Other"] * (1 - building_operation / 100)
}

# Data for the bar chart
energy_data = {
    "Base Case": base_energy_data,
    "Improved": improved_energy_data
}

# Dummy investment cost data
investment_cost = {
    "Base Case": 500,
    "Improved": 500 * (1 - (thermal_envelope + heating_system + ventilation_system + renewable_energy + building_operation) / 500)
}

# Calculate energy consumption per year/m2
energy_consumption = {
    "Base Case": sum(base_energy_data.values()),
    "Improved": sum(improved_energy_data.values())
}

# Display energy consumption bar chart
st.subheader("Energy consumption (kWh/m²/y)")
energy_df = pd.DataFrame(energy_data).T
fig, ax = plt.subplots()
energy_df.plot(kind="bar", stacked=True, ax=ax, color=sns.color_palette("muted"))
ax.set_ylabel("Energy Consumption (kWh/m²/y)")
ax.set_title("Energy Consumption by Type")
st.pyplot(fig)

# Display investment cost vs. energy cost
st.subheader("Investment cost vs. energy cost")
investment_df = pd.DataFrame(list(investment_cost.items()), columns=["Case", "Cost"])
fig, ax = plt.subplots()
sns.barplot(x="Case", y="Cost", data=investment_df, palette="muted", ax=ax)
ax.set_ylabel("Cost")
ax.set_title("Investment Cost Comparison")
st.pyplot(fig)

# Additional features
st.sidebar.header("Additional Features")
energy_level = st.sidebar.selectbox("Energy level", ["Low", "Medium", "High"])
hot_water_supply = st.sidebar.checkbox("Include hot water supply")
carbon_intensity = st.sidebar.selectbox("Select fuel type and grid carbon intensity", ["Low", "Medium", "High"])

# Placeholder for future features
st.sidebar.header("Future Features")
budget = st.sidebar.number_input("Provide budget")
tool_advice = st.sidebar.checkbox("Tool advice on best strategy")

# Display carbon emission savings (dummy data)
carbon_savings = 20  # Placeholder value
st.subheader("Carbon emission savings")
st.write(f"Estimated carbon emission savings: {carbon_savings} kg CO2/m²/y")

# Placeholder image to represent the building
st.image("https://via.placeholder.com/400", caption="Example building")

st.write("""
This is a mockup of the BIM4Energy Case Study Explorer. 
You can select different parameters on the sidebar to see how it affects the energy consumption and investment costs.
""")
