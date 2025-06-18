import os

questions = ["今は西暦何年ですか？",
             "今は令和何年ですか？",
             "今日は何月何日ですか？"]

f = open("answer.txt", "w")

for i, question in enumerate(questions):
    userInput = input("{}: ".format(question))
    f.write(userInput)
    if not question == questions[-1]:
        f.write(", ")


f.close()
