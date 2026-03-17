class WaitTimeAgent:
    def predict_wait(self, queue_state):
        queue_length = queue_state["queue_length"]
        service_time = queue_state["service_time"]
        counters = queue_state["open_counters"]

        wait_time = (queue_length * service_time) / counters
        return round(wait_time, 2)