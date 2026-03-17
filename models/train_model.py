import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample dataset
data = {
    "queue_length": [5, 10, 15, 20, 8, 12, 18, 6],
    "arrival_rate": [2, 4, 6, 8, 3, 5, 7, 2],
    "service_time": [2, 3, 4, 5, 2, 3, 4, 2],
    "open_counters": [2, 2, 3, 3, 2, 2, 3, 1],
    "wait_time": [6, 12, 18, 25, 9, 14, 22, 7]
}

df = pd.DataFrame(data)

X = df[["queue_length", "arrival_rate", "service_time", "open_counters"]]
y = df["wait_time"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved")