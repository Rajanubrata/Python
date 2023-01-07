from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)
while quiz.still_has_question():
    quiz.next_question()
