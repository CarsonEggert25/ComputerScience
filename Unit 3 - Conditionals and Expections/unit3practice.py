# Boolean Expression
# Kinda like a mathmatical formula
# Can only evaluate to true or false
# are my shoes tied? > true
# is 5 > 7 + false
print(5 > 7)

# comparison operators! == > < >= <=
# Kinda like arithmetic operators! + - / * ** % //
x = 5                   # SET x equal to 5, tell it what to be
print(x == 5)           # GET x equals 5, ask a question
#The diffrence is that we are using one or two equal signs
#This is a perfect test question

print(4 >= 2)       #true
print(1993 == 1993) #true
print(-90 < -99)    #false
print(10 != 10)     #false, "bash" "not"


#Boolean expressions quiz
answer_one = input("give me a integer that is negative")
answer_one = int(answer_one)
print(answer_one < 0)

answer_2 = input("write the number 5\n>")
# answer_2 = int(answer_2) this is unnecessary!
print(answer_2 == "5")

print("walrus" == "walrus")     # == is totally valid for 2 strings


# If statements evaluate boolean expressions
# Make decisions about which code to run next

# Take a temperature
# print "<temperature> is hot" if the temperature is >= 80
# Otherwise, print "<temperature> is not hot"
temperature = input("what is the temperature\n>")
temperature = int(temperature)
# if, boolean expression, :
# sort of like a function, no parenthesis!
if temperature >= 80:
    print("The temperature is " + str(temperature) + " degrees.") 
    print(str(temperature) + " is hot outside")

else:   #else takes NO condition and runs when the if above false
    # Otherwise.......
    print("The temperature is " + str(temperature) + " degrees.") 
    print(str(temperature) + " degrees is not hot")

password = input("what is the password\n>")
password =int(password)
if password == "skibidi68":
    print("access granted")
else:
    print("access denied")

real_answer1 = "fortnite"
input_question = input("what is the best battle royale ever?\n>")
if input_question == real_answer1:
    print("correct answer")
else:
    print("wrong aswer")
real_answer2 = "interstellar"
input_question2 = input("what is the best movie ever created?\n>")
if input_question2 == real_answer2:
    print("correct answer")
else:
    print("wrong answer")

# string functions
# A group of like-functions that munipulate strings
# modify strings
# super easy and convenient to use
# python would really not be fun without them
    
#   .lower()
# converts a string to all lowercase
# no matter what the input casing is, it is converted to lowercase
# and the answer is lowercase
input_answer = "Lord Of The Rings"
input_answer = input_answer.lower() #converts to lord of he rings
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
# coverts a string to uppercase!
x = "hello world".upper()
print(x)    # prints HELLO WORLD

# .capitalize
# converts to lowercase, then capitalizes the first letter 
y = "HeLlO wOrLd".capitalize()
print(y)        # print "hello world"

# .title()
# converts a string to a titlecase
#capital first letters of words
z = "HeLlo world".title()
print(z)

#.swapcse
#it intverts the casing of each character
q = "HeLlo WoRld".swapcase()
print(q)


x = 0

if x > 0:
    print("x is a positive number!")

elif x < 0:     #elif statements are always paired to an if 
    print("x is a negative number!")

else:       #else statements are always paired to an if statements 
            #else statements never take a condition 
    print("x is a zero")


color = input("what color is the light")

if color.lower == "green":      #only one if 
    print("go")

elif color.lower == "red":      # No limit to how many elifs you can use
    print("stop")

elif color.lower() == "yellow":
    print("stop if safe")

else:                               # only one else
    print("call the police")

# why do i even need elif statements???
# Can't I just use more if's?
    
x = 10

if x > 5:
    print("x is greater than five")

if x > 8:
    print("x is greater than eight")

############################
    
if x > 5:
    print("x is greater than five")

elif x > 8:
    print("x is greater than eight")

