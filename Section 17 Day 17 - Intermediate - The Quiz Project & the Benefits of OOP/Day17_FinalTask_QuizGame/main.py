from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for d in question_data:
    # question_bank.append(Question(d["text"], d["answer"]))
    question_bank.append(Question(d["question"], d["correct_answer"]))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
