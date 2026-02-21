def engineer_features(df):
    df["StudyHours_sq"]=df["StudyHours"]**2
    df["Age_StudyHours"]=df["Age"] * df["StudyHours"]
    return df