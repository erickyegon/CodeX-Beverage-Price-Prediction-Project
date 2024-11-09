import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pathlib import Path

def load_model():
    model_path = r"C:\Users\User\Documents\RFM model\codebasics\internships\Data Science\Codex Project\models\best_model.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def get_price_range(category):
    """
    Get price range for each category
    """
    ranges = {
        'Budget': '₹100 - ₹149',
        'Economy': '₹150 - ₹199',
        'Premium': '₹200 - ₹249',
        'Luxury': '₹250 - ₹299'
    }
    return ranges[category]

def prepare_input_features(input_data):
    """
    Prepare input features matching the training data encoding
    """
    # Initialize feature array with zeros
    feature_array = np.zeros(25)
    current_idx = 0
    
    # 1. Label encoded features
    age_group_map = {'18-25': 0, '26-35': 1, '36-45': 2, '46-55': 3, '55+': 4}
    income_map = {'16L - 25L': 0, '26L - 35L': 1, '35L+': 2}
    health_map = {'Low': 0, 'Medium': 1, 'High': 2}
    freq_map = {'1-2': 0, '3-4': 1, '5-7': 2}
    size_map = {'Small': 0, 'Medium': 1, 'Large': 2}

    feature_array[0] = age_group_map[input_data['age_group']]
    feature_array[1] = income_map[input_data['income_levels']]
    feature_array[2] = health_map[input_data['health_concerns']]
    feature_array[3] = freq_map[input_data['consume_frequency']]
    feature_array[4] = size_map[input_data['preferable_size']]
    
    # 2. Numeric features
    feature_array[5] = int(input_data['current_brand_score'])
    feature_array[6] = int(input_data['zone_awareness'])
    feature_array[7] = int(input_data['brand_satisfaction'])
    feature_array[8] = int(input_data['brand_awareness'])
    
    current_idx = 9
    
    # 3. One-hot encoded features
    # Gender
    if input_data['gender'] == 'F':
        feature_array[current_idx] = 1
    current_idx += 1
    
    # Zone
    zone_idx = {'Tier 1': 0, 'Tier 2': 1, 'Rural': 2}
    if input_data['zone'] in zone_idx:
        feature_array[current_idx + zone_idx[input_data['zone']]] = 1
    current_idx += 3
    
    # Occupation
    occ_idx = {'Salaried': 0, 'Student': 1, 'Self-employed': 2, 'Other': 3}
    if input_data['occupation'] in occ_idx:
        feature_array[current_idx + occ_idx[input_data['occupation']]] = 1
    current_idx += 4
    
    # Current Brand
    brand_idx = {'New': 0, 'None': 1}
    if input_data['current_brand'] in brand_idx:
        feature_array[current_idx + brand_idx[input_data['current_brand']]] = 1
    current_idx += 2
    
    # Flavor Preference
    flavor_idx = {'Modern': 0, 'Mixed': 1}
    if input_data['flavor_preference'] in flavor_idx:
        feature_array[current_idx + flavor_idx[input_data['flavor_preference']]] = 1
    current_idx += 2
    
    # Purchase Channel
    channel_idx = {'Retail': 0, 'Both': 1}
    if input_data['purchase_channel'] in channel_idx:
        feature_array[current_idx + channel_idx[input_data['purchase_channel']]] = 1
    current_idx += 2
    
    # Packaging Preference
    package_idx = {'Modern': 0, 'Premium': 1}
    if input_data['packaging_preference'] in package_idx:
        feature_array[current_idx + package_idx[input_data['packaging_preference']]] = 1
    
    return pd.DataFrame([feature_array])

def main():
    st.set_page_config(
        page_title="CodeX Beverage Price Predictor",
        page_icon="🥤",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for better styling and compact layout
    st.markdown("""
        <style>
        .main-header {
            font-size: 2rem;
            color: #1E88E5;
            text-align: left;
            margin-bottom: 0.5rem;
            padding-top: 0rem;
        }
        .sub-header {
            font-size: 1rem;
            color: #424242;
            margin-bottom: 1rem;
        }
        .stButton button {
            width: 100%;
        }
        .section-header {
            font-size: 1rem;
            color: #1E88E5;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        .prediction-header {
            font-size: 1.2rem;
            color: #1E88E5;
            text-align: center;
            margin: 0.5rem 0;
        }
        div[data-testid="stVerticalBlock"] {
            padding-top: 0rem;
        }
        div[data-testid="stHorizontalBlock"] {
            padding-top: 0rem;
        }
        div.row-widget.stSelectbox {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        div.row-widget.stButton {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
        .element-container {
            margin-bottom: 0.5rem;
        }
        .stMarkdown {
            margin-bottom: 0rem;
        }
        .stMetric {
            margin-bottom: 0rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header row with instructions
    header_col1, header_col2 = st.columns([2, 1])
    
    with header_col1:
        st.markdown('<p class="main-header">CodeX Beverage Price Predictor</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Developed by Dr. Erick K. Yegon - Data Science Project</p>', unsafe_allow_html=True)
    
    with header_col2:
        with st.expander("📝 Instructions", expanded=True):
            st.markdown("""
            1. Fill in all fields below
            2. Click 'Calculate Price Range'
            3. Price categories:
               - **Budget**: ₹100-149
               - **Economy**: ₹150-199
               - **Premium**: ₹200-249
               - **Luxury**: ₹250-299
            """)

    # Load model silently
    try:
        model = load_model()
    except Exception as e:
        st.error("Error loading the prediction model. Please try again later.")
        return

    # Create three columns for inputs with reduced spacing
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("##### Demographics")
        age_group = st.selectbox("Age Group", 
                                options=['18-25', '26-35', '36-45', '46-55', '55+'],
                                key='age')
        gender = st.selectbox("Gender", options=['M', 'F'])
        zone = st.selectbox("Zone", options=['Metro', 'Tier 1', 'Tier 2', 'Rural'])
        occupation = st.selectbox("Occupation", 
                                options=['Entrepreneur', 'Salaried', 'Student', 'Self-employed', 'Other'])
        income_levels = st.selectbox("Income Level", 
                                   options=['16L - 25L', '26L - 35L', '35L+'])
    
    with col2:
        st.markdown("##### Consumption Patterns")
        consume_frequency = st.selectbox("Weekly Consumption", 
                                       options=['1-2', '3-4', '5-7'])
        current_brand = st.selectbox("Current Brand", 
                                   options=['Established', 'New', 'None'])
        preferable_size = st.selectbox("Size", 
                                     options=['Small', 'Medium', 'Large'])
        brand_awareness = st.selectbox("Brand Awareness", 
                                     options=['0', '1', '2', '3', '4', '5'])
        current_brand_score = st.selectbox("Brand Score", 
                                         options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    
    with col3:
        st.markdown("##### Preferences")
        zone_awareness = st.selectbox("Zone Awareness", 
                                    options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        brand_satisfaction = st.selectbox("Satisfaction", 
                                        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        health_concerns = st.selectbox("Health Concerns", 
                                     options=['Low', 'Medium', 'High'])
        flavor_preference = st.selectbox("Flavor", 
                                       options=['Traditional', 'Modern', 'Mixed'])
        purchase_channel = st.selectbox("Purchase Channel", 
                                      options=['Online', 'Retail', 'Both'])
        packaging_preference = st.selectbox("Packaging", 
                                          options=['Simple', 'Modern', 'Premium'])

    # Calculate button and prediction in the same row
    button_col, pred_col1, pred_col2 = st.columns([1, 2, 1])
    
    with button_col:
        calculate_button = st.button("Calculate Price Range", type="primary", use_container_width=True)

    if calculate_button:
        input_data = {
            'age_group': age_group,
            'gender': gender,
            'zone': zone,
            'occupation': occupation,
            'income_levels': income_levels,
            'consume_frequency': consume_frequency,
            'current_brand': current_brand,
            'preferable_size': preferable_size,
            'brand_awareness': brand_awareness,
            'current_brand_score': current_brand_score,
            'zone_awareness': zone_awareness,
            'brand_satisfaction': brand_satisfaction,
            'health_concerns': health_concerns,
            'flavor_preference': flavor_preference,
            'purchase_channel': purchase_channel,
            'packaging_preference': packaging_preference
        }
        
        try:
            features_df = prepare_input_features(input_data)
            prediction = model.predict(features_df)
            price_ranges = ['Budget', 'Economy', 'Premium', 'Luxury']
            predicted_range = price_ranges[prediction[0]]
            price_bracket = get_price_range(predicted_range)
            
            with pred_col1:
                st.metric(
                    label="Recommended Price Category",
                    value=f"{predicted_range} ({price_bracket})"
                )
                
        except Exception as e:
            with pred_col1:
                st.error("Error calculating price range. Please try different inputs.")

if __name__ == "__main__":
    main()
