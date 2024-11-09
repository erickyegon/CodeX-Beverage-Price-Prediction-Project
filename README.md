# CodeX-Beverage-Price-Prediction-Project

## Project Background
CodeX, a German beverage company entering the Indian market, needed a sophisticated price prediction system to optimize their product pricing strategy. The company aims to establish a strong presence in the Indian energy drink segment with data-driven pricing decisions that consider various customer demographics and market factors.

Key business metrics include:
- Market Entry: New entrant in Indian market
- Business Model: Premium beverage manufacturer
- Key Metrics: Price optimization, market segmentation, customer preferences

The company's primary focus is ensuring optimal pricing across different market segments, with particular attention to regional variations and customer preferences.

## Model Development and Deployment

### MLflow Experiment Tracking
The project utilizes MLflow for experiment tracking and model management. Multiple models were evaluated:
- Gaussian NB
- SVM (cv_score: 0.78789, std: 0.009934)
- Logistic Regression
- Random Forest
- XGBoost
- LightGBM

All experiments and model metrics are tracked in MLflow for reproducibility and comparison.

### Model Deployment
- **Live Application**: [CodeX Price Predictor App](https://codex-beverage-price-prediction-project-unq9a4tkr7sm5zahq2xuvx.streamlit.app/)
- **Platform**: Streamlit Cloud
- **Real-time Predictions**: Instant price category recommendations
- **User Interface**: Interactive web-based interface

## Insights and Recommendations:

### Category 1: Model Performance
- Main Insight 1: Model achieves accurate price predictions across four distinct categories
- Main Insight 2: Price predictions aligned with market segments (Budget to Luxury)
- Main Insight 3: Feature engineering significantly improved prediction accuracy
- Main Insight 4: Customer segmentation enhanced model performance

### Category 2: Customer Segmentation
- Main Insight 1: Demographics strongly influence price sensitivity
- Main Insight 2: Clear patterns emerged in consumption preferences
- Main Insight 3: Income levels correlate with price category predictions
- Main Insight 4: Regional variations show distinct pricing patterns

### Category 3: Feature Analysis and Importance
- Main Insight 1: Age and income are primary drivers of price predictions
- Main Insight 2: Brand awareness impacts pricing strategy
- Main Insight 3: Health consciousness influences price sensitivity
- Main Insight 4: Purchase channels affect pricing decisions

### Category 4: Streamlit Deployment
- Main Insight 1: Successfully deployed user-friendly interface
- Main Insight 2: Real-time predictions for price optimization
- Main Insight 3: Scalable solution for business growth
- Main Insight 4: Easy integration with existing systems

## Data Structure & Initial Checks
The model processes various input parameters across multiple categories:

1. Demographics Data:
   - Age Group
   - Gender
   - Zone
   - Occupation
   - Income Level

2. Consumption Patterns:
   - Weekly Consumption
   - Current Brand
   - Size Preference
   - Brand Awareness
   - Brand Satisfaction

3. Market Insights:
   - Zone Awareness
   - Health Concerns
   - Flavor Preferences
   - Purchase Channels
   - Packaging Preferences

## Executive Summary

### Overview of Findings
The analysis shows that accurate price prediction requires considering multiple factors including demographics, consumption patterns, and market dynamics. The model successfully categorizes prices into four segments: Budget (₹100-149), Economy (₹150-199), Premium (₹200-249), and Luxury (₹250-299).

### Three Key Insights:
1. Demographics significantly influence price sensitivity
2. Consumption patterns indicate clear price preferences
3. Market factors drive regional pricing variations

## Technical Implementation

### Model Features
- Input Processing: 25 processed features
- Encoding Methods: Label, One-hot, and Numeric scaling
- Prediction Categories: 4 price ranges
- Real-time Processing: Streamlit interface
- Experiment Tracking: MLflow
- Model Registry: Version control and deployment management

### Deployment Stack
- Web Framework: Streamlit
- Experiment Tracking: MLflow
- Model Serving: Streamlit Cloud
- Version Control: Git

## Author
Dr. Erick K. Yegon

## Links
- [Live Deployment](https://codex-beverage-price-prediction-project-unq9a4tkr7sm5zahq2xuvx.streamlit.app/)
- [GitHub Repository](https://github.com/erickyegon/codebasics_internship)
- [MLflow Dashboard](https://dagshub.com/erickyegon/codebasics_internship/experiments)

## Conclusion
The CodeX Price Prediction system provides accurate, data-driven pricing recommendations across different market segments. Through sophisticated feature engineering, MLflow experiment tracking, and an intuitive Streamlit interface, it enables strategic pricing decisions for the Indian market entry.
