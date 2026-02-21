from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate(models):
    results = {}
    
    for name, (model, X_test, y_test) in models.items():
        y_pred = model.predict(X_test)
        rmse  = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)

        results[name] = {
            "RMSE": rmse,
            "R2": r2,
            "Coefficients": model.coef_
        }
    
    return results