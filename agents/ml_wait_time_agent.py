import joblib

class MLWaitTimeAgent:

    def __init__(self):
        self.model = joblib.load("models/model.pkl")

    def predict(self, queue_state):

        X = [[
            queue_state["queue_length"],
            queue_state["arrival_rate"],
            queue_state["service_time"],
            queue_state["open_counters"]
        ]]

        wait = self.model.predict(X)[0]

        return round(wait,2)