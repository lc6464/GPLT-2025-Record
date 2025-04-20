count, finished = input().split(" ")

questions = []
for _ in range(int(count)):
    question = input()
    if 'qiandao' in question or 'easy' in question:
        continue
        
    questions.append(question)

finished = int(finished)
if len(questions) <= finished:
    print("Wo AK le")
else:
    print(questions[finished])