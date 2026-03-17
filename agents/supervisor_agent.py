from agents.queue_observer import QueueObserverAgent
from agents.wait_time_agent import WaitTimeAgent
from agents.congestion_agent import CongestionAgent
from agents.staff_agent import StaffAgent
from agents.optimization_agent import OptimizationAgent
from agents.customer_assistant import CustomerAssistantAgent
from agents.location_agent import LocationAgent


class SupervisorAgent:
    def run_system(self):
        observer = QueueObserverAgent()
        wait_agent = WaitTimeAgent()
        congestion_agent = CongestionAgent()
        staff_agent = StaffAgent()
        optimization_agent = OptimizationAgent()
        location_agent = LocationAgent()

        queue_state = observer.observe_queue()
        wait_time = wait_agent.predict_wait(queue_state)
        congestion = congestion_agent.detect_congestion(queue_state)
        staff = staff_agent.recommend_staff(queue_state)
        optimization = optimization_agent.optimize_queue(queue_state)
        best_branch = location_agent.recommend_branch()

        return {
            "queue_state": queue_state,
            "predicted_wait_time": wait_time,
            "congestion": congestion,
            "recommended_counters": staff,
            "optimization": optimization,
            "best_branch": best_branch
        }