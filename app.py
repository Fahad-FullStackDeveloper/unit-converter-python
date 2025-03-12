import streamlit as st

# App Metadata
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# App Title
st.title("🔄 Unit Converter")
st.write("Easily convert between different units of Length, Weight, Temperature, and Area.")

# Conversion Options
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Area"])

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


def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "Square Meter": 1,
        "Square Kilometer": 0.000001,
        "Square Centimeter": 10000,
        "Square Millimeter": 1000000,
        "Square Mile": 0.000000386102,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550.0031,
        "Acre": 0.000247105,
        "Hectare": 0.0001,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# User Input
if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    value = st.number_input("Enter Length", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_length(value, from_unit, to_unit)

elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce", "Ton"]
    value = st.number_input("Enter Weight", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_weight(value, from_unit, to_unit)

elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter Temperature", format="%.2f")
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_temperature(value, from_unit, to_unit)

else:
    units = ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Acre", "Hectare"]
    value = st.number_input("Enter Area", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    result = convert_area(value, from_unit, to_unit)

# Display Result
st.metric(label=f"Converted Value ({to_unit})", value=round(result, 2))

# Developer Info
st.sidebar.header("📌 Developer Info")
st.sidebar.write("**Developer:** Fahad Khakwani")
st.sidebar.write("**Version:** 1.1.0")
st.sidebar.write("**Tech Used:** Python, Streamlit")
st.sidebar.write("🚀 Upgrade this app by adding more conversions like Speed and Time!")

# Version History
st.sidebar.subheader("📜 Version History")
st.sidebar.write("- **v1.0.0 (2025-03-12):** Initial release with basic conversions (Length, Weight, and Temperature).")
st.sidebar.write("- **v1.1.0 (2025-03-13):** Added Area conversions (Square Meter, Square Kilometer, Acre, Hectare, etc.)")

# Upcoming Upgrades
st.sidebar.subheader("🚀 Upcoming Upgrades")
st.sidebar.write("- Add Speed conversion (m/s, km/h, mph, knots, etc.)")
st.sidebar.write("- Add Time conversion (seconds, minutes, hours, days, weeks, etc.)")
st.sidebar.write("- Improve UI with better color themes and input validations.")
