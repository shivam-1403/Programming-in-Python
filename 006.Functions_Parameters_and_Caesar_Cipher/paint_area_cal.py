# This is an area calculator, where you will calculate an area of wall, and find out how much cans of paint are required if one can covers 5 meter squares of area.

import math

def paint_req(height, width, cover):
    area= height*width
    paint=area/coverage
    num_cans=math.ceil(paint)
    print(f"You'll need {num_cans} cans of paint.")

coverage=5
test_h=int(input("Enter the height of the wall : "))
test_w=int(input("Enter the width of the wall : "))

paint_req(test_h, test_w, coverage)