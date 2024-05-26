import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Dummy data for energy consumption and investment costs
energy_data = {
    "Base Case": {"Heating": 100, "Cooling": 50, "Other": 30},
    "Improved": {"Heating": 50, "Cooling": 20, "Other": 10}
}
investment_cost = {"Base Case": 500, "Improved": 300}

# Calculate energy consumption per year/m2
energy_consumption = {
    "Base Case": sum(energy_data["Base Case"].values()),
    "Improved": sum(energy_data["Improved"].values())
}

# Display energy consumption bar chart
st.subheader("Energy consumption (kWh/m²/y)")
energy_df = pd.DataFrame(energy_data).T
energy_df.plot(kind="bar", stacked=True)
st.pyplot(plt)

# Display investment cost vs. energy cost
st.subheader("Investment cost vs. energy cost")
investment_df = pd.DataFrame(list(investment_cost.items()), columns=["Case", "Cost"])
st.bar_chart(investment_df.set_index("Case"))

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
