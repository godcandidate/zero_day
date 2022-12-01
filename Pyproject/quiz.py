import json

# Opening JSON file
f = open('quiz.json', )
data = json.load(f)
i = 0;

questions = []
for item in data['results']:
	if i == 2:
		break
	question = item['question']
	questions.append(question)
	i += 1
for item in questions:
	print(item)
