from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# from dict to object
q_data = question_data
question_bank = []

# for item in range(0, len(question_data)):
#     question_bank.append(Question(q_data[item]["text"], q_data[item]["answer"]))

for question in question_data[0]["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz.")
print(f"Your final score: {quiz.score}/{quiz.question_number}")