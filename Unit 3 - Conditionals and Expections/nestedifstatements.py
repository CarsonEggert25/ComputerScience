#  Nested if statements
# you are a prime member OR order is at least $25
# you are at least 18 years OR have parent consent

prime = True
Cost = 20
Age = 17
Consent = False

if prime:
    if Age >=18:
        print("you are eligible for free shipping!")
    elif Consent:
        print("you are eligible for free shipping!")
    else:
        print("you are NOT eligible for free shipping!")

elif Cost >=25:
    if Age >=18:
        print("you are eligible for free shipping!")
    elif Consent:
         print("you are eligible for free shipping!")
    else:
        print("you are NOT eligible for free shipping!")

else:
    print("you are NOT eligible for free shipping!")

        

# Do we need an umbrella?
    
# We need an umbrella id it is raining and we are outside
raining = input("is it raining today?")


if raining.lower() == "yes":
    outside = input("Are you going outisde today?")
    
    if outside.lower() == "yes":
        print("bring an umbrella")
    else:
        print("dont bring an umbrella")

else:
    print("don't bring an umbrella")

