from question_model import Question
from data import question_data

q_data = question_data
list_of_questions = []

for item in range(0, len(question_data)):
    list_of_questions.append(Question(item["text"], item["answer"]))

print(list_of_questions)