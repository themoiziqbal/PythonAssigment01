import streamlit as st

# Apply custom styles
st.markdown(
    """
    <style>
    body {
        background-color: #f0f3f6;
    }
    .stApp {
        background-color:rgb(216, 252, 255);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .stTextInput, .stSelectbox, .stNumberInput {
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color:rgb(83, 185, 236);
        color: white;
        font-size: 16px;
        padding: 8px 16px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color:rgb(62, 160, 150);
    }
    .success-box {
        font-size: 18px;
        font-weight: bold;
        color: #4CAF50;
        background-color: #e7f5e9;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Converter functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000,
        'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1, 'grams': 1000, 'milligrams': 1000000, 'pounds': 2.20462, 'ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        return (value * 9/5 + 32) if to_unit == "fahrenheit" else value + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "fahrenheit" else value
    return value

# Main function
def main():
    st.markdown("<h1 style='color:#008CBA; text-align:center;'>🌟 Unit Converter 🌟</h1>", unsafe_allow_html=True)
    
    # Sidebar
    conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
    
    # Input value
    value = st.number_input("Enter Value", value=0.0)

    # Layout for unit selection
    col1, col2 = st.columns(2)
    if conversion_type == "Length":
        with col1:
            from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
        with col2:
            to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    elif conversion_type == "Weight":
        with col1:
            from_unit = st.selectbox("From", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
        with col2:
            to_unit = st.selectbox("To", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    elif conversion_type == "Temperature":
        with col1:
            from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
        with col2:
            to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])

    # Convert button
    if st.button("🔄 Convert"):
        if conversion_type == "Length":
            result = length_converter(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = weight_converter(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = temp_converter(value, from_unit, to_unit)
        
        # Display result
        st.markdown(f"<div class='success-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
