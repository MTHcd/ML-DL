
class HumanFeedback:
    def __init__(self, model, feedback_data):
        self.model = model
        self.feedback_data = feedback_data

    def process_feedback(self):
        print("Processing human feedback:", self.feedback_data)
    