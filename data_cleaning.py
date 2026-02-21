import pandas as pd
import numpy as np

def load_and_clean_data():
    data = {
        "Name": ["Aman", "Riya", "Karan", "Sneha", "Arjun", "Meera", "Rohit", "Priya"],
        "Gender": ["M", "F", "M", "F", "M", "F", "M", "F"],
        "Marks": [78, np.nan, 67, 92, 45, 85, np.nan, 73],
        "StudyHours": [4, 6, 3, 8, 2, 7, 5, np.nan],
        "Age": [20, 21, 19, 22, 18, 20, 21, 19]
    }
    
    
    df = pd.DataFrame(data)
    

    df["Marks"].fillna(df["Marks"].mean(), inplace=True)
    df["StudyHours"].fillna(df["StudyHours"].median(), inplace=True)
    
    return df