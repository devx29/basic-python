import area_and_volume as av
from rpsls import rpsls_game

print(f"Area of Square is {av.area_formula_square}")
print(f"Area of Circle is {av.area_formula_circle}")

av.area(Length = 8, Radius = 6)

print(__name__)
print(av.__name__)

rpsls_game()

