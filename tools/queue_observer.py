import random

def observe_queue():

    queue_state = {
        "queue_length": random.randint(5,25),
        "service_time": random.randint(2,4),
        "arrival_rate": random.randint(3,10),
        "open_counters": random.randint(1,4)
    }

    return queue_state