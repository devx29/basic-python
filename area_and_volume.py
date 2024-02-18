import math
#calculate area/volume for a square/cube and circle/sphere

area_formula_circle = "Pi x (Radius x Radius)"
area_formula_square = "Length x Length"

volume_formula_sphere = "4/3 x Pi x (Radius x Radius x Radius)"
volume_formula_cube = "Length x Length x Length"

def area(**input):
    area_of_square = math.pow(int(input['Length']), 2)
    area_of_circle = (math.pi) * (math.pow(int(input['Radius']), 2))
    print(f"Area of Square with Length {input['Length']} is {area_of_square:.2f}")
    print(f"Area of Circle with Radius {input['Radius']} is {area_of_circle:.2f}")

if __name__ == "__main__":
    area(Length = 9, Radius = 7)