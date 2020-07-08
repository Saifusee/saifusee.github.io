#functions 1
import sys
from f2 import square
try:
    number = int(input("NUMBER: "))
except ValueError:
    print("ERROR : INPUT MUST BE INTEGER")
    sys.exit(1)
#starting of our function same as we are impoting from f2.py
def square(number):
    return number * number
#end of our funcion

    
print(f"THE SQUARE OF GIVEN NUMBER IS {square(number)}")

#here check this i made a variable named number to take some input from users specifically integer input 
#and then create a new function name square whose work is to just multiply the variable whose it taking as input with that variable again
#then i print the end result.
#####important point i ensure the indentations before print else program don't run.