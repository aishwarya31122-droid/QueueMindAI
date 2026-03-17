class CongestionAgent:
    def detect_congestion(self, queue_state):
        q = queue_state["queue_length"]

        if q < 8:
            return "LOW"
        elif q < 15:
            return "MEDIUM"
        else:
            return "HIGH"