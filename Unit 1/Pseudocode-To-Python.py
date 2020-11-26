marks = [84,58,23,60]
counter = 4

#This is a bubble sort program 

while counter > 1:
    for sort in range(3):
        if marks[sort] > marks[sort+1]:
            #Switches the two indexes between one another.
            switch = marks[sort]
            marks[sort] = marks[sort+1]
            marks[sort+1] = switch

    counter =- 1

#This is only one pass and will output as that only.

print(marks)