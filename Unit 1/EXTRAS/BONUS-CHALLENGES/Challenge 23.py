def fibbonaci(iterations):
    a = 0
    b = 1
    for x in range(iterations+1):
        print(a) #outputs the sequence
        c = a + b # placeholder for a + b since a gets changed before b and vice versa, this would make the function incorrect otherwise.
        a = b
        b = c

def fibbonaci_reverse(iterations):
    a = 0
    b = 1
    fibbonaci_list = []
    for x in range(iterations+1):
        fibbonaci_list.append(a) #outputs the sequence
        c = a + b # placeholder for a + b since a gets changed before b and vice versa, this would make the function incorrect otherwise.
        a = b
        b = c

    for i in reversed(fibbonaci_list):
        print(i)


def fibbonaci_total(iterations):
    a = 0
    b = 1
    total = 0
    for x in range(iterations+1):
        c = a + b # placeholder for a + b since a gets changed before b and vice versa, this would make the function incorrect otherwise.
        a = b
        b = c
        total += a
    print(f"Total : {total}")
    
def menu_logic(user_input, iterations):
    if user_input == "default":
        return fibbonaci(iterations)
    if user_input == "reverse":
        return fibbonaci_reverse(iterations)
    if user_input == "total":
        return fibbonaci_total(iterations)
    else:
        main()

def main():

    user_specifed_iteration_limit = int(input("How many times do you want the sequence to repeat? : "))
    user_specifed_function = str(input("What function would you like to use (default, reverse or total)? : "))
    menu_logic(user_specifed_function, user_specifed_iteration_limit)

main()