import math

lawn_dimensions = float(input("Lawn Dimensions (in Metres) : "))
flowerbed_radius = float(input("Flowerbed Radius (in Metres) : "))

circle_area = math.pi * flowerbed_radius

print(f"Amount of Turf Required {circle_area} Sq Metres")