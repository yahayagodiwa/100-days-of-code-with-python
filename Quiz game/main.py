from data import question_data

class Question:
    def __init__(self, text,  answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_question(self):
        curent_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f" Q. {self.question_number}: {curent_question.text} (true/false): ")
        self.check_answer(user_answer, curent_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right ")
            self.score += 1
        else:
           print("You got it wrong ")
        print(f"The correct answer is {correct_answer} ")
        print(f"Your current score is {self.score}/{self.question_number} ")


    def still_hasQuestion(self):
        return self.question_number < len(self.question_list)
           

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_hasQuestion:
    quiz.next_question()

print("You have completed the quiz")
print(f"Your total score is {quiz.score}/{len(question_bank)}")