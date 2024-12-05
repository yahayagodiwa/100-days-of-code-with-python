
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        
    def next_question(self):
        curent_question = self.question_list[self.question_number]
        input(f"Q. {self.question_number}: {curent_question.text} (true/false): ")