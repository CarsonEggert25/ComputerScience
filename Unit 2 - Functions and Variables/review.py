print("Hello, world!")              # "hello, world!" is the parameter
input("please enter your username\n>")  # \n is called an escape character
# \n starts a new line (linebreak)
# input is never required

#variables
#syntax
#<name> = <value>
x = 5

#snake naming convention - all lowercase, underscore for spaces
# concise: short and descriptive
username = "osowski"        #define string
fav_animal = "calugo"       #define string
total_poptarts = 12         #define integers (whole numbers)
percent_complete = 23.52    #define float (decimal number)
is_cool = True              #define boolean (true/false)
first_letter = 'c'          #define character (single symbol)

total_poptarts = 8          #reassign



# Arithmetic operations
# + - * / ** % //
print(4 + 4)          #> 8
print("4 + 4")        #> 44
print("cat" + "dog")  #> catdog
print("cat" * 3)      #>catcatcat
print ("cat" + 3)     #> ERROR: cannot use + for string and int

# make some working programs
# 1. add two numbers using input
x = int(input("what is x?\n>"))      # input() always return as a string
y = input("what is y?\n>")      # even if you type in a number 
y = int(y)                          #covert from string to int
print(x + y)

# 2. converts celcious to farenheight
temp_celcius = input("what is the temp in celcius")
temp_celcius = int(temp_celcius)
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + " degrees F ")



# some coversion factors
str()
int()
float()
bin()
bool()

# the stuff that goes between the parenthesis is called parameters
# parameter are the values that the function needs to run

# functions 
# functions are a lot like varibles 
# they have names
# they can be recalled from memory by calling their name 
# store information
# varibles store valvues, functions store code
def potato():       # def keyword + name + () + :
    print("potato") # lines indented underneath are "inside" the function

# functions are not ran when they are defined 
# they must be called by their name to run
potato()    # every function call needs open and closed parenthesis
            # even if it has no parameters

def jump(how_high):
    print(" you jumped " + str(how_high) + " inches! ")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k,):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("c", "a", "r", "s" "o", "n")

#functions can have many many lines
def top_ten_games():
    print("1. elden ring")
    print("2. shadow of colossus")
    print("3. minecraft")
    print("4. diablo 3")
    print("5. fortnite")
    print("6. rocket league")
    print("7. world of warcraft")
    print("8. path pf exile")
    print("9. enter the gungeon")
    print("10. gta 5")

#scope: global and local varibles!!
#scope refers to the context in which the varible was defined 
#GLOBAL- defined at no indentation level
#LOCAL- defined inside of a function

#global varibles can be used anywhere
todd = "cool guy"       #global varible- no indentation level

#local varibles only exist in the scope they were defined 
def my_function():
    smith = "not cool guy"  #local varible- define in a function
    todd = "strange guy"    #local varibles even though it has the same name 
    print(todd)             #prints the local varible todd
    # when you call a varible in a function
    # it searches local varibles first, then global varibles

#if you want to reassign a global varible inside a function
todd = "cool guy"
def my_function2():
    global todd         #in ths function, whenevr I call todd
                        # I mean the global todd, not the local
    todd = "strange guy"    #reassign todd- global
    print(todd)             # print todd - global

#return functions
#functions cam also retuen values
#the value that is returned is sent back to where the function is called 
#this is very similar to how varibles work
#the function does its work and retuen the answer back
def add2(x, y):
    return x + y    #returns the sum of x and y to where the function is called

answer = add2(2, 10)    #retuen