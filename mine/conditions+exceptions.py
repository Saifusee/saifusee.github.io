import sys
try:
    x = int(input("NUMBER: "))
except ValueError:
    print("INVALID INPUT, Type a Number not a word")
    sys.exit(1)

if x > 0 :
    print("Given Number is Positive.")
elif x < 0 :
        print("Given Number is negative")
else :
    print("Given Number is Neutral")
 