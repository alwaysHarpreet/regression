from data_cleaning import load_and_clean_data
from feature_engineering import engineer_features
from train_model import train_models
from model_evaluation import evaluate

df = load_and_clean_data()
df = engineer_features(df)

X = df.drop("Marks", axis=1)
y = df["Marks"]

X = X.drop(["Name", "Gender"], axis=1)

trained_models = train_models(X, y)
results = evaluate(trained_models)

for model, metrics in results.items():
    print(f"\n{model}")
    for k, v in metrics.items():
        print(f"{k}: {v}")