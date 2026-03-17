class CustomerAssistantAgent:

    def answer_question(self, question, queue_info):

        wait = queue_info["predicted_wait_time"]
        congestion = queue_info["congestion"]

        question = question.lower()

        if "wait" in question:
            return f"The current estimated waiting time is {wait} minutes."

        elif "busy" in question or "congestion" in question:
            return f"The current congestion level is {congestion}."

        elif "visit" in question or "best time" in question:
            if congestion == "LOW":
                return "This is a good time to visit. Queue traffic is low."
            else:
                return "Queues are currently busy. You may want to visit later."

        else:
            return "I can answer questions about waiting time, congestion, and best time to visit."