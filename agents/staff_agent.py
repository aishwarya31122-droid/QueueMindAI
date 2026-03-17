class StaffAgent:
    def recommend_staff(self, queue_state):
        queue_length = queue_state["queue_length"]

        if queue_length < 8:
            return 2
        elif queue_length < 15:
            return 3
        else:
            return 4