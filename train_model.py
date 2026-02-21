from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler

def train_models(X,y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state = 42
    )
    
    scaler = StandardScaler()
    X_trained_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    models = {
        "Linear": LinearRegression(),
        "Ridge": Ridge(alpha = 0.1),
        "Lasso": Lasso(alpha=0.1)
    }
    
    trained = {}
    
    for name, model in models.items():
        model.fit(X_trained_scaled, y_train)
        trained[name] = (model, X_test_scaled, y_test)
        
    return trained