from string import ascii_lowercase
import json
import random

# Opening JSON file
f = open('quiz.json', )
data = json.load(f)

num_correct = 0
questions = random.sample(data['results'], k=4)

for num,(item) in enumerate(questions, start=1):
	if num == 3:
		break;

	#storing the variables
	question = item['question']
	correct_answer = item['correct_answer']
	alternatives = item['incorrect_answers']
	alternatives.append(item['correct_answer'])

	sorted_alternatives = sorted(alternatives)

	# display
	print(f"{num}. {question}?")

	labeled_alternatives = dict(zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))

	#check if option is in
	for label, alternative in labeled_alternatives.items():
		print(f"  {label}) {alternative}")

	while (answer_label := input("\nEnter choice: ")) not in labeled_alternatives:
        	print(f"Please answer one of {', '.join(labeled_alternatives)}")

	answer = labeled_alternatives[answer_label]

	if answer == correct_answer:
		num_correct += 1
		print("⭐ Correct! ⭐")
	else:
		print(f"The answer is {correct_answer!r}, not {answer!r}")


print(f"\nYou got {num_correct} correct out of {num} questions")
