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


def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "Square Meter": 1,
        "Square Kilometer": 0.000001,
        "Square Centimeter": 10000,
        "Square Millimeter": 1000000,
        "Hectare": 0.0001,
        "Acre": 0.000247105,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "Meter per Second": 1,
        "Kilometer per Hour": 3.6,
        "Mile per Hour": 2.23694,
        "Foot per Second": 3.28084,
        "Knot": 1.94384,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        "Liter": 1,
        "Milliliter": 1000,
        "Cubic Meter": 0.001,
        "Gallon": 0.264172,
        "Quart": 1.05669,
        "Pint": 2.11338,
        "Cup": 4.16667,
        "Fluid Ounce": 33.814,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


def convert_pressure(value, from_unit, to_unit):
    conversion_factors = {
        "Pascal": 1,
        "Kilopascal": 0.001,
        "Bar": 0.00001,
        "PSI": 0.000145038,
        "Atmosphere": 0.00000986923,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_currency(value, from_unit, to_unit):
    conversion_rates = {
        "USD": 1,
        "EUR": 0.91,
        "GBP": 0.78,
        "INR": 82.75,
        "PKR": 277.5,
        "AUD": 1.53,
        "CAD": 1.35,
        "JPY": 149.1,
        "CNY": 7.12,
        "SAR": 3.75,
        "AED": 3.67,
        "CHF": 0.88,
    }
    return value * (conversion_rates[to_unit] / conversion_rates[from_unit])

# User Input
if conversion_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    result = convert_length
elif conversion_type == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce", "Ton"]
    result = convert_weight
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    result = convert_temperature
elif conversion_type == "Area":
    units = ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", "Hectare", "Acre"]
    result = convert_area
elif conversion_type == "Speed":
    units = ["Meter per Second", "Kilometer per Hour", "Mile per Hour", "Foot per Second", "Knot"]
    result = convert_speed
elif conversion_type == "Time":
    units = ["Second", "Minute", "Hour", "Day"]
    result = convert_time
elif conversion_type == "Volume":
    units = ["Liter", "Milliliter", "Cubic Meter", "Gallon", "Quart", "Pint", "Cup", "Fluid Ounce"]
    result = convert_volume
elif conversion_type == "Pressure":
    units = ["Pascal", "Kilopascal", "Bar", "PSI", "Atmosphere"]
    result = convert_pressure
elif conversion_type == "Currency":
    units = ["USD", "EUR", "GBP", "INR", "PKR", "AUD", "CAD", "JPY", "CNY", "SAR", "AED", "CHF"]
    result = convert_currency
else:
    result = None

value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
st.metric(label=f"Converted Value ({to_unit})", value=round(result(value, from_unit, to_unit), 2))

# Sidebar Info
st.sidebar.header("📌 Developer Info")
st.sidebar.write("**Developer:** Fahad Khakwani")
st.sidebar.write("**Version:** 1.5.1")
st.sidebar.write("**Tech Used:** Python, Streamlit")

# Version History
st.sidebar.subheader("📌 Version History")
st.sidebar.write("1.0.0 - Basic conversions: Length, Weight, Temperature")
st.sidebar.write("1.1.0 - Added Area conversions")
st.sidebar.write("1.2.0 - Added Speed conversions")
st.sidebar.write("1.3.0 - Added Time conversions")
st.sidebar.write("1.4.0 - Added Volume & Pressure conversions")
st.sidebar.write("1.4.1 - Name changed to **Advanced Unit Converter**")
st.sidebar.write("1.5.0 - Added Currency conversions (12 Currencies)")
st.sidebar.write("1.5.1 - Upcoming Upgrades")

# Upcoming Upgrades
st.sidebar.subheader("🚀 Upcoming Upgrades")
st.sidebar.write("✔️ Power conversions")
st.sidebar.write("✔️ Data Storage conversions")
st.sidebar.write("✔️ Fuel Efficiency conversions")
st.sidebar.write("✔️ Watt Conversion (Power, Voltage, Current, Resistance)")
st.sidebar.write("✔️ Energy conversions")
st.sidebar.write("✔️ Force conversions")
st.sidebar.write("✔️ Torque conversions")
st.sidebar.write("✔️ Cooking Measurement conversions")
st.sidebar.write("✔️ Electric Charge conversions")
st.sidebar.write("✔️ Electric Current conversions")
st.sidebar.write("✔️ Voltage conversions")
st.sidebar.write("✔️ Acceleration conversions")
st.sidebar.write("✔️ Density / Mass per Volume conversions")
st.sidebar.write("✔️ Charge Capacity conversions")
st.sidebar.write("✔️ Common Conversion Units for Power Watt (W), Kilowatt (kW), Megawatt (MW), Horsepower (HP), Joule per second (J/s), BTU per hour (BTU/h), Calorie per second (cal/s) conversions")
