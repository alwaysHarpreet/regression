# Student Performance Predictor

## Problem Statement
Predict student marks using study behavior and demographics.

## Dataset
Synthetic academic dataset with cleaned missing values.

## Feature Engineering
- Squared study hours for non-linearity
- Age-study interaction for maturity effect

## Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression

## Evaluation Metrics
RMSE and R²

## Key Findings
- Ridge improved stability
- Lasso simplified the model by removing weak features

## Limitations
- Small dataset
- No psychological or historical features

## Future Improvements
- Add consistency-based features
- Try tree-based models

## Verdict
“Linear Regression severely overfit due to small dataset and correlated engineered features. Ridge stabilized coefficient magnitudes and significantly reduced error. Lasso further simplified the model by eliminating weak features, demonstrating automatic feature selection. Although R² remained negative due to limited data size, RMSE improved substantially, highlighting the importance of regularization in practical regression tasks.”