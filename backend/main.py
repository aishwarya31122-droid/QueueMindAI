import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools.queue_observer import observe_queue
from tools.predict_wait import predict_wait
from agents.optimization_agent import optimize_queue


queue = observe_queue()

wait_time = predict_wait(
    queue["queue_length"],
    queue["service_time"],
    queue["arrival_rate"]
)

decision = optimize_queue(
    wait_time,
    queue["queue_length"],
    queue["open_counters"]
)

print("Queue State:", queue)
print("Predicted Wait:", wait_time)
print("AI Decision:", decision)