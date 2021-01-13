y = []
forbidden_numbers = [3,6]
for x in range(7):
    if x in forbidden_numbers:
        continue
    else:
        y.append(x)

print(y)