#classes 1
#how to create a class
import sys
class coordinates():
    def __init__(self, input1, input2, input3):
      self.x = input1
      self.y = input2
      self.z = input3
try:
   xval = int(input("x: "))
   yval = int(input("y : "))
   zval = int(input("z : "))
except ValueError:
    print("ERROR: Requires a Integer")
    sys.exit(1)
c = coordinates(xval, yval, zval)
print(f"The given Coordinates are({c.x}, {c.y}, {c.z})")
