import random
from quiz_questions import questions

score = 0
selected_questions = random.sample(questions, len(questions))

for q in selected_questions:
    answer = input(q["question"] + " ")
    if answer.strip().lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", q["answer"])

print("\nYour score:", score, "/", len(questions))