import streamlit as st

# App Metadata
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔄", layout="centered")

# App Title
st.title("🔄 Advanced Unit Converter")
st.write("Easily convert between different units of Length, Weight, Temperature, Area, Speed, Time, Volume, Pressure, and Currency.")

# Conversion Options
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Area", "Speed", "Time", "Volume", "Pressure", "Currency"])

# Conversion Logic

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
        "Ounce": 35.274,
        "Ton": 0.001,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32


def convert_currency(value, from_unit, to_unit):
    conversion_rates = {
        "USD": 1,
        "EUR": 0.85,
        "GBP": 0.75,
        "INR": 74.5,
        "JPY": 110,
        "CNY": 6.45,
    }
    return value * (conversion_rates[to_unit] / conversion_rates[from_unit])

# User Input
if conversion_type == "Currency":
    units = ["USD", "EUR", "GBP", "INR", "JPY", "CNY"]
    result = convert_currency
elif conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    result = convert_length
elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce", "Ton"]
    result = convert_weight
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    result = convert_temperature

value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
st.metric(label=f"Converted Value ({to_unit})", value=round(result(value, from_unit, to_unit), 2))

# Sidebar Info
st.sidebar.header("📌 Developer Info")
st.sidebar.write("**Developer:** Fahad Khakwani")
st.sidebar.write("**Version:** 1.5.0")
st.sidebar.write("**Tech Used:** Python, Streamlit")

# Version History
st.sidebar.subheader("📌 Version History")
st.sidebar.write("1.0.0 - Basic conversions: Length, Weight, Temperature")
st.sidebar.write("1.1.0 - Added Area conversions")
st.sidebar.write("1.2.0 - Added Speed conversions")
st.sidebar.write("1.3.0 - Added Time conversions")
st.sidebar.write("1.4.0 - Added Volume & Pressure conversions")
st.sidebar.write("1.4.1 - Name changed to **Advanced Unit Converter**")
st.sidebar.write("1.5.0 - Added Currency conversions")

# Upcoming Upgrades
st.sidebar.subheader("🚀 Upcoming Upgrades")
st.sidebar.write("✔️ Energy conversions")
st.sidebar.write("✔️ Power conversions")
