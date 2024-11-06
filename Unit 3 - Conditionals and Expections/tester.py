def start_adventure(): #time to begin reeheehee
    print("You wake up at 7:15 AM on what you think to be an ordinary wednseday. Do you:")
    print("1. Get up for school")
    print("2. Sleep in")


    choice_1 = input("> ")

    if choice_1 == "1":
        go_to_school()
    elif choice_1 == "2":
        sleep_in()
    else:
        print("Invalid choice, try again")
        start_adventure()

    
  

def go_to_school():
    print("Okay Mr. Goody Two-Shoes, you get up for school, get ready, and walk out to the bus stop. After 20 minutes, the bus finally arrives. Do you:")
    print("1. Sit in the front")
    print("2. Sit in the middle")
    print("3. Sit in the back")
    choice_2 = input("> ")
    if choice_2 == "1":
        sit_on_bus()
    if choice_2 == "2":
        sit_on_bus()
    elif choice_2 == "3":
        sit_on_bus()
    else:
        print("Try again bucko")
       
        go_to_school ()


def sleep_in():
    print("Good choi- uh, i mean, skipping school is like, bad. Buuut you made the decision so, congratulations! You sleep until 12:00 PM. You decide to go have some breakfast, in the afternoon... Do you:")
    print("1. Make some cereal - the easiest choice")
    print("2. Actually put in effort and cook a meal - takes longer")
    choice_3 = input("> ")
    if choice_3 == "1":
        make_cereal()
    elif choice_3 == "2":
        cook_breakfast()
    else:
        print("Dude, just pick one of the options")
        sleep_in()

def cook_breakfast():
    print("You decide you're gonna make a full meal. You make...")
    print("1. Eggs and bacon")
    print("2. Pancakes")
    print("3. Toast...")
    print("4. All of the above")
    choice_8 = input("> ")
    if choice_8 == "1":
        fight()
    elif choice_8 == "2":
        fight()
    elif choice_8 == "3":
        print("thats lame...")
        fight()
    elif choice_8 == "4":
        print("FATTY")
        fight()
    else:
        print("PICK A VALID OPTION BRO")
        cook_breakfast()

def fight():
    





def sit_on_bus():
    print("You sit down on the bus. It is relatively quiet. Almost, too quiet...")
    print("...")
    
def make_cereal():
    print("You go in your pantry and take a look. You see a few different types of cereal. You pick:")
    print("1. Frosted Flakes")
    print("2. Another cereal thats inferior to Frosted Flakes...")
    choice_4 = input("> ")
    if choice_4 == "2":
        print("Weirdo...")
        eat_cereal()
    elif choice_4 == "1":
        eat_cereal()
    else:
        print("its not that hard bro, just pick a cereal")
        make_cereal()


def eat_cereal():
    print("While you're eating your cereal, KSI suddenly busts through the door and starts ranting about screens and pens and how hes the king and the crown is his bling...or something like that. He then asks you if his new song is good. You say:")
    print("1. Bro, your song sucks")
    print("2. I like your song man. I'm also gonna buy Lunchly")
    choice_5 = input("> ")
    if choice_5 == "1":
        KSI_freakout()
    elif choice_5 == "2":
        KSI_talk()
    else:
        print("Just...pick...")
        eat_cereal()

def KSI_talk():
    print("KSI doesn't believe you since everyone else has been laughing at his song so he assumes that you're lying")
    KSI_freakout()




def KSI_freakout():
    print("KSI starts screaming about how his song is great and how you're wrong. He then challenges you to a boxing match. At the match you decide to give yourself an 'advantage'")
    print("1. Eat a mushroom from Super Mario Bros")
    print("2. Phone a friend")
    print("3. Spin the mystery box")
    print("4. Use the FLDSMDFR from Cloudy with a Chance of Meatballs")
    choice_6 = input("> ")
    if choice_6 == "1":
        super_mushroom_win()
    elif choice_6 == "2":
        phone_friend()
    elif choice_6 == "3":
        mystery_box()
    elif choice_6 == "4":
        flint_lockwood()
    else:
        ("Please pick an actual option, okay?")
        KSI_freakout()

def mystery_box():
    print("You decide to spin the mystery box. After it rolls for a while you get...")
    import random
    r = random.randrange(0,1)
    print (r)
    if r == 0:
        print("a good item")
        good_item()
    elif r == 1:
        print("a bad item")
        bad_item()

    
        mystery_box()
    


def good_item():
    print("You open the box and get a good item. Its good enough to beat KSI")
    print("You beat KSI and become the new co-owner of Prime and Lunchly (You probably don't want to though)")
    


def bad_item():
    print("The item you get is terrible. KSI beats you with no effort and you go into hiding")
    game_over()


def flint_lockwood():
    print(" You use the FLDSMDFR to make it rain moldy lunchly cheese. Everyone in the stadium gets sick and it starts an epidemic of illness from lunchly")
    game_over()




def super_mushroom_win():
    print("You eat the mushroom and quadriple in size. You stomp out to the arena, destroying everything in your path. You stomp on KSI and win the fight with ease. Congratulations, you beat the game without dying!")

def phone_friend():
    print("You take out your phone. Who do you call?")
    print("1. Gumball Watterson")
    print("2. Spongebob Squarepants")
    print("3. Caseoh")
    print("4. Mr. Beast")
    choice_7 = input("> ")
    if choice_7 == "1":
        call_gumball()
    elif choice_7 == "2":
        call_spongebob()
    elif choice_7 == "3":
        call_caseoh()
    elif choice_7 == "4":
        call_mr_beast()
    else:
        print("Dude, is it really that hard to pick a valid answer? (Hint: Its not...)")
    phone_friend()


def call_gumball():
    print("You call Gumball ... ... ... The phone goes to voicemail. He...didn't pick up... He was too lazy...")
    lose_boxing_gumball()


def lose_boxing_gumball():
    print("You go into the ring with no help since Gumball didn't answer the phone. KSI wins the match with no effort and you are forced to go into hiding as to not face the humiliation from society. ")
    game_over()


def game_over():
    print("GAME OVER")


def call_caseoh():
    print("Caseoh rips off the roof of the arena, towering over it with his massive body. He then opens his mouth and everything starts getting sucked into it. You, KSI, and everyone else in the building get eaten by Caseoh.")
    game_over()
    


def call_mr_beast():
    print("You call Mr. Beast to see if he can call off KSI. He agrees but only if you promise to help with his next video '100 kids vs 100 kids who have pencils. You agree to help and he calls off KSI. Congratulations, you beat the game AND you get a free Lunchly! Just be careful with the cheese...")


start_adventure()