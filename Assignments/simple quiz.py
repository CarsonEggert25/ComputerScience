real_answer1 = "fortnite"
input_question = input("what is the best battle royale ever?\n>")
if input_question == real_answer1:
    print("correct answer")
    x = 1
else:
    print("wrong aswer")
    x = 0
real_answer2 = "interstellar"
input_question2 = input("what is the best movie ever created?\n>")
if input_question2 == real_answer2:
    print("correct answer")
    x = x + 1
else:
    print("wrong answer")
real_answer3 = "vanilla"
input_question3 = input("what is the best ice cream flavor?\n>")
if input_question3 == real_answer3:
    print("correct answer")
    x = x + 1
else:
    print("wrong answer")
real_answer4 = "bench press"
input_question4 = input("what is the best chest workout?\n>")
if input_question4 == real_answer4:
    print("correct answer")
    x = x + 1
else:
    print("wrong answer")
real_answer5 = "summer"
input_question5 = input("what is the best season of all?\n>")
if input_question5 == real_answer5:
    print("correct answer")
    x = x + 1
else:
    print("wrong answer")

print("total score. " + str(x) + "/5")