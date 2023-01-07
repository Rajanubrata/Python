class QuizBrain:

    def __init__(self, obj):
        self.question_number =0
        self.question_list = obj
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True\False): ")
        self.check_ans(user_answer.lower(), current_question.answer.lower())


    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True


    def check_ans(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1
            print("You get it correct! ")
        else:
            print("You get this wrong")
        print(f"Correct answer is = {correct_ans}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")
