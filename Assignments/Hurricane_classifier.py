print("what are the speeds of diffrent catergory hurricanes")

MPH = int(input("how many miles per hour are the wind speeds"))

if MPH.lower < 74:
    print("tropical storm")
elif MPH.lower < 96:
    print("category 1")
elif MPH.lower < 111:
    print("category 2")
elif MPH.lower < 130:
    print("category 3")
elif MPH.lower < 157:
    print("category 4")
elif MPH.lower >= 157:
    print("category 5")
else:
    print("call for help")