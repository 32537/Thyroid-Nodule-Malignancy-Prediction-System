# Run Command  ：python.exe -m streamlit run Web Application\Web.py

from pycaret.classification import *
import streamlit as st
import numpy as np
import random
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Thyroid Nodule Malignancy Prediction",
    page_icon="🏥",
    layout="centered"
)

# Fix random seeds
np.random.seed(42)
random.seed(42)

# Load model
@st.cache_resource
def load_model_func():
    return load_model(r'Web Application\Logistic Regression')

loaded_model = load_model_func()

# Dictionary definitions
Gender_dict = {"Male": 0, "Female": 1}
Composition_dict = {'Others': 0, 'Solid': 1}
Shape_dict = {'Others': 0, 'Microlobulated': 1}
Echogenicity_dict = {'Others': 0, 'Hypoechogenicity': 1}
Echogenic_foci_dict = {'Others': 0, 'Microcalcification': 1}
Margin_dict = {'Smooth': 0, 'Irregular': 1}
ATR_dict = {'Wider_than_tall': 0, 'Taller_than_wide': 1}
Peri_BFS_dict = {'Absent': 0, 'Less': 1, 'Rich': 2}
Pathological_diagnosis_dict = {0: 'Benign', 1: 'Malignant'}
						

# Page title and description
st.title("🏥 Thyroid Nodule Malignancy Prediction System")
st.markdown("---")
st.markdown("Please provide the following ultrasound examination features to predict the probability of nodule malignancy")

# Create two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Information")
    
    # Gender
    Gender = st.selectbox(
        label='Gender',
        options=('Male', 'Female'),
        index=1,
        help='Please select your gender'
    )

    # Age
    Age = st.number_input(
        label='Age (years)',
        min_value=0,
        max_value=120,
        value=30,
        step=1,
        help='Please enter your age'
    )

    # Maximum diameter
    Maximum_diameter = st.number_input(
        label='Maximum Diameter (mm)',
        min_value=0.0,
        max_value=100.0,
        value=0.5,
        step=0.1,
        format='%.1f',
        help='Please enter the maximum diameter of the nodule'
    )

with col2:
    st.subheader("Ultrasound Features")
    
    # Peripheral blood flow signal
    Peri_BFS = st.selectbox(
        label='Peripheral Blood Flow Signal (Peri_BFS)',
        options=('Absent', 'Less', 'Rich'),
        index=0,
        help='Select peripheral blood flow signal status'
    )

    # Composition
    Composition = st.selectbox(
        label='Composition',
        options=('Others', 'Solid'),
        index=0,
        help='Select nodule composition'
    )

    # Shape
    Shape = st.selectbox(
        label='Shape',
        options=('Microlobulated', 'Others'),
        index=0,
        help='Select nodule shape characteristics'
    )

# Create second row with two columns
col3, col4 = st.columns(2)

with col3:
    # Echogenicity
    Echogenicity = st.selectbox(
        label='Echogenicity',
        options=('Others', 'Hypoechogenicity'),
        index=1,
        help='Select echogenicity'
    )

    # Echogenic foci
    Echogenic_foci = st.selectbox(
        label='Echogenic Foci',
        options=('Others', 'Microcalcification'),
        index=1,
        help='Select echogenic foci characteristics'
    )

with col4:
    # Margin
    Margin = st.selectbox(
        label='Margin',
        options=('Smooth', 'Irregular'),
        index=0,
        help='Select nodule margin characteristics'
    )

    # ATR (Aspect Ratio)
    ATR = st.selectbox(
        label='Aspect Ratio (ATR)',
        options=('Wider_than_tall', 'Taller_than_wide'),
        index=0,
        help='Select nodule aspect ratio characteristics'
    )

# Data processing
predict_data = pd.DataFrame({
    'Age': [Age],
    'Gender': [Gender_dict[Gender]],
    'Maximum_Diameter': [Maximum_diameter],
    'Peri_BFS': [Peri_BFS_dict[Peri_BFS]],
    'Composition': [Composition_dict[Composition]],
    'Shape': [Shape_dict[Shape]],
    'Echogenicity': [Echogenicity_dict[Echogenicity]],
    'Echogenic_Foci': [Echogenic_foci_dict[Echogenic_foci]],
    'Margin': [Margin_dict[Margin]],
    'ATR': [ATR_dict[ATR]]
})

st.markdown("---")

# Prediction button and result display
if st.button("🔍 Predict Now", type="primary", use_container_width=True):
    with st.spinner('Analyzing data, please wait...'):
        prediction = predict_model(loaded_model, data=predict_data, raw_score=True, probability_threshold=0.4821)
    
    # Get prediction results
    prediction_label = prediction.iloc[0]['prediction_label']
    
    if prediction_label == 0:
        prediction_score = prediction.iloc[0]['prediction_score_0'] * 100
    else:
        prediction_score = prediction.iloc[0]['prediction_score_1'] * 100
    
    # Display results
    st.markdown("### 📊 Prediction Results")
    
    # Use color coding for results
    if prediction_label == 1:
        st.error(f"**Predicted Class**: {Pathological_diagnosis_dict[prediction_label]}")
        st.error(f"**Malignancy Probability**: {prediction_score:.2f}%")
    else:
        st.success(f"**Predicted Class**: {Pathological_diagnosis_dict[prediction_label]}")
        st.success(f"**Benign Probability**: {prediction_score:.2f}%")
    
    # Generate recommendations
    st.markdown("### 💡 Recommendations")
    if prediction_label == 1:
        advice = (
            f"Based on our model analysis, your thyroid nodule has a high risk of malignancy. "
            f"The model predicts a malignancy probability of {prediction_score:.1f}%. "
            "This is only a preliminary assessment. We recommend consulting a thyroid specialist "
            "as soon as possible for further evaluation, such as fine-needle aspiration biopsy, "
            "to obtain an accurate diagnosis and timely treatment plan."
        )
        st.warning(advice)
    else:
        advice = (
            f"Based on our model analysis, your thyroid nodule is likely benign. "
            f"The model predicts a benign probability of {prediction_score:.1f}%. "
            "We recommend regular ultrasound follow-ups to monitor any changes in the nodule, "
            "and maintaining a healthy lifestyle. Please seek medical attention promptly "
            "if you experience any symptoms."
        )
        st.info(advice)

# Disclaimer
st.markdown("---")
st.caption("⚠️ **Disclaimer**: This prediction is for reference only and does not replace professional medical diagnosis. Please consult a healthcare professional for accurate diagnosis.")