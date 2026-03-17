import random

class QueueObserverAgent:
    def observe_queue(self):
        queue_state = {
            "queue_length": random.randint(5, 20),
            "arrival_rate": random.randint(2, 8),
            "service_time": random.randint(2, 5),
            "open_counters": random.randint(1, 4)
        }
        return queue_state