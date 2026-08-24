'''This will find the square of any whole number in the range
   -10000000 to 10000000 the user inputs'''

Answ = input("This will find the square of any number, please input a number: ")
Num = int(Answ)
if Num in range(-1000000,1000000):
    print(Num**2)
else: print("you either put a number too large or small (the range is (-10000000,10000000)) or not a number at all!")
