import random
from datetime import datetime, timedelta

class QueueSimulator:

    def simulate_customers(self, n=500):

        data = []

        current_time = datetime.now()

        for i in range(n):

            customer = {
                "customer_id": i + 1,
                "arrival_time": (current_time + timedelta(seconds=i*5)).strftime("%H:%M:%S"),
                "service_time": random.randint(2,6),
                "queue_length": random.randint(1,25)
            }

            data.append(customer)

        return data