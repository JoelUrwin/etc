import random

number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0

array = []

def randomizer():
    for x in range(6):
        randomnumber = random.randint(1,49)
        if randomnumber in array:
            randomnumber = random.randint(1,49)
        if randomnumber not in array:
            array.append(randomnumber)

randomizer()
array.sort()
print(array)