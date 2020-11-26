marks = [84,58,23,60]
counter = 4

while counter > 1:
    for sort in range(3):
        if marks[sort] > marks[sort+1]:
            switch = marks[sort]
            marks[sort] = marks[sort+1]
            marks[sort+1] = switch

    counter =- 1

print(marks)