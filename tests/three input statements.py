print ("three random input statments")                         #title
user_input1 = input("please type one random word\n>")       #type in one random word
user_input2 = input("please type another random word\n>")   #type in a second random word
user_input3 = input("please type a third random word\n>")   #type in a third random word
print (" your first word is " + user_input1 + " your second word is " + user_input2 + " your third word is " + user_input3) # a summary of the data collected

def add():
    print("add three numbers:")                         #title
    x = (input("what is the first integer?\n>"))        #type in your first number
    x = int(x)                                          # x= the number you put in
    y = (input("what is the second integer?\n>"))       #type in your second number
    y = int(y)                                          #y= second number you put in
    z = (input("what is the third integer?\n>"))        #type in your third number
    z = int(z)                                          # z= third number you put in
    print(str(x) + " + " + str(y) + " + " + str(x) + " = " + str(x + y + z))    # your three numbers added together

add()       #add function

def data_three():                                   
    print("add three types of data")                #title
    word_input = input("please type in a word\n>")  #type in a word
    integer_input = input("please type in a intager\n>") #type in a integer
    float_input = input("please type in a float\n>")    # type in a float
    print(" your first statement " + word_input + " your second statement " + integer_input + " your third statement " + float_input) #summary of data collected

add()       #add function




