from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data :
    ques = Question(q["text"], q["answer"])
    question_bank.append(ques)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions() :
    quiz.next_question()
print("You Have Completed The Quiz !")
print(f"Your Final Score was : {quiz.score}/{quiz.question_number}")