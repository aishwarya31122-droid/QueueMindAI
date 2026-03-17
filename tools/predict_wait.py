import joblib
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

model = joblib.load(model_path)

def predict_wait(queue_length,service_time,arrival_rate):

    X = np.array([[queue_length,service_time,arrival_rate]])

    prediction = model.predict(X)

    return float(prediction[0])