text
# Gold Price Prediction Using Machine Learning (Regression)

## Overview
This project predicts daily gold prices using machine learning regression models. Gold prices are influenced by macroeconomic indicators such as stock indices, currency exchange rates, and commodity prices. This system helps investors, traders, and policymakers make data-driven decisions about buying or selling gold.

## Dataset
The dataset FINAL_USO.csv contains historical data including:

Independent Features (Inputs):
- SP_close – S&P 500 closing price
- DJ_close – Dow Jones Industrial Average closing price
- USDI_Price – U.S. Dollar Index value
- EU_Price – Euro price level
- PLT_Price – Platinum price
- USO_Close – Crude Oil ETF closing price
- Volume – Gold trading volume

Dependent Feature (Target):
- Close – Gold daily closing price

## Libraries Used
- numpy, pandas – Data manipulation
- matplotlib, seaborn – Data visualization
- scikit-learn – Machine learning models & metrics
- pickle, joblib – Model saving and loading
- time – Timestamp for logging

## Data Analysis & Visualization
- Scatter plots to study relationships between gold prices and features
- Correlation heatmap to identify feature importance
- Combined analysis report with multiple visualizations in dark mode for better readability

## Machine Learning Models Tested
- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regressor (SVR)

Best Model: Random Forest Regressor
Performance on Test Set:
- R² Score: 0.992
- RMSE: 2.11

## Model Training
- Split data into training and testing sets (80/20)
- Trained all models and compared performance using R² score and RMSE
- Visualized model comparison using barplots in dark theme

## Model Testing & Prediction
- Predicted vs actual gold prices plotted for performance evaluation
- Cross-validation (optional) for model robustness
- Saved trained Random Forest model: random_forest_model.pkl

## Usage
1. Load dataset: FINAL_USO.csv
2. Train the model or load the pre-trained model:
   import joblib
   model = joblib.load("random_forest_model.pkl")
3. Prepare input features and make predictions:
   y_pred = model.predict(x_test)
4. Evaluate predictions using R² score or RMSE.

## Visual Outputs
- Scatter plots of gold price vs features
- Correlation heatmap
- Combined report: Gold_Price_Report.png
- Model comparison plots: Model_Compare_R2_dark.png, Model_Compare_RMSE_dark.png
- Predicted vs actual plot: Predicted_vs_actual.png

## Author
Siddiqa Ali
