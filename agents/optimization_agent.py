class OptimizationAgent:
    def optimize_queue(self, queue_state):
        queue_length = queue_state["queue_length"]
        counters = queue_state["open_counters"]

        if queue_length > 15:
            decision = "Open an additional counter"
        elif queue_length < 5 and counters > 1:
            decision = "Reduce one counter"
        else:
            decision = "Current setup is optimal"

        return decision