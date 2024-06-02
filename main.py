from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_q = Question(i.get("question"), i.get("correct_answer"))
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the Quiz.")
print(f"Your final score was {quiz.score}/{len(question_bank)}")

