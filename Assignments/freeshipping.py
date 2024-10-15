def Free_shipping(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("free shipping applied!")
    else:
        print("ineligible for free shipping")
        
p = False
s = 100
a = 80
c = True

Free_shipping(p, s, a, c)