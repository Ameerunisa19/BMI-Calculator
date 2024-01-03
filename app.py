import streamlit as st
from PIL import Image

# BMI categories
bmi_categories = {
    (0, 18.5): "Underweight : Build Strength 💪",
    (18.5, 25): "Healthy : Optimal Balance ⚖️",
    (25, 30): "Overweight : Healthy Choices Ahead 🥦",
    (30, float("inf")): "Obese : Transformation Time 🌟"
}

# Display a styled title using HTML/CSS
st.markdown("""
    <h1 style='text-align: center;'>BodyShape IQ🏋️‍♀️</h1>
    <h5 style='text-align: left;'>BMI (Body Mass Index) is a numerical measure that assesses your body weight in relation to your height. It provides insights into your overall health and fitness.<br>BMI Categories :</h5>
<h5 style='text-align: left; margin-left: 70px;'>🦴 Underweight : Build Strength 💪<br>🍏 Healthy : Optimal Balance ⚖️<br>🍔 Overweight : Healthy Choices Ahead 🥦<br>🍩 Obese : Transformation Time 🌟<br></h5>
<h5 style='text-align: left;'>Achieving a healthy BMI is an essential step towards a fit and active lifestyle💪</h5>
""", unsafe_allow_html=True)

# Load and display images
images = ["main.jpg", "scale.jpg"]
for img_path in images:
    img = Image.open(img_path)
    st.image(img, use_column_width=True)

# Input for weight and height
weight = st.number_input("Enter your Weight in **KG**", step=0.1, format="%f")
height = st.number_input("Enter Your Height in **Centimeters**", step=1, format="%d")

# Calculate BMI
if weight > 0 and height > 0:
    height_Centimeters = height / 100.0
    bmi = weight / (height_Centimeters ** 2)

    # Display BMI
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # Determine BMI category
    for (lower, upper), category in bmi_categories.items():
        if lower <= bmi < upper:
            st.success(f"**You are** **{category}**")

    # Recommendations based on BMI
    if bmi < 18.5:
        st.warning("Consider consulting a doctor for being underweight. 🩺")
    elif bmi >= 30:
        st.warning("Consider consulting a doctor for obesity and healthy lifestyle changes. 🏥")
    else:
        st.success("You are in the healthy weight range. Maintain a balanced lifestyle for good health. 🥗💪")
