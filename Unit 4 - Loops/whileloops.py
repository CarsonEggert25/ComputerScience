#There are a couple types of loops in python
#The for loop lets your iterate a list
#-Great for looping a set of number of times
#But WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password
# You could get it right the first time
# It could take you a million tries
# Or anything in between

real_pass = "potato45"
entered_pass = ""

attempts = 0
# A while loop continues looping until the condition is no longer true
while real_pass != entered_pass:        # check if the entered password matches the real one
    # Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts = attempts +1

    #check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + " attempts.")
        print("try again...")

# End password checking
print("Welcome!")



# With while loops, you need to be careful for infinite loops
# When you put your computer in rest mode, it has nightmares about infinite loops /joke
# An infinite loop happens when you enter a while loop that can never be escaped
# example (do not click run)

# count = 0
#While true:
#       count += 1
#       print(count)

#Print("ALL done")

# Real world Example
#"type "exit" to quit

user_input = " "

while user_input != "Exit":
    user_input = input("enter something (type 'exit' to quit)")
    print("you entered" + user_input)
    
print("all done")

