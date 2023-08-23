import json

with open("questions.json", "r") as file:
    content = file.read() #this is a string

data = json.loads(content) #this is a list

for dictionary in data:
    print(dictionary["question_text"])
    for index, alternative in enumerate(dictionary["alternatives"]):
        print(index +1,"-", alternative)
    user_choice = int(input("enter your answer: "))
    dictionary["user_choice"] = user_choice
    
score = 0    
for index, dictionary in enumerate(data):
    if dictionary["user_choice"] == dictionary["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result} {index +1} - Your answer: {dictionary['user_choice']}, " \
          f"Correct answer: {dictionary['correct_answer']}"
    print(message)



print(score, "/", len(data))