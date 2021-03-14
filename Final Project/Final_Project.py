questions = ["How many days do we have in a week",
"What element does 'O' represent on the periodic table?",
"What's the name of the river that runs through Egypt?",
"What's the highest mountain in the world?",
"What is the capital of Spain",
"What is the capital of Turkey",
"How many letters in the word hippopotamus?",
"Which animal is known as the 'King of jungle?'",
"Which is the largest country in the world?",
"In which direction does the sunrise?"]

answers = ["7", "oxygen", "nile", "everest", "madrid", "ankara", "12", "lion", "russia", "east"]

point = 0
length_array = len(questions)

for i in range(length_array):
    print(questions[i])
    user_answer = input("Please write your answer in lower case: ")
    if user_answer == answers[i]:
        point += 10

if point > 50:
    print(f'Well Done!!! Your point is: {point}')
else:
    print(f'This is pathetic :( Your point is: {point}')
