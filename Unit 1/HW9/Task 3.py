def centimetres_to_inches():
    centimetres = float(input(f"Input Centimetres : "))
    inches = centimetres / 2.54
    return print(f"{centimetres} Centimetres is equal to {centimetres}in")

def inches_to_centimetres():
    inches = float(input(f"Input Inches : "))
    centimetres = inches * 2.54
    return print(f"{inches} Inches is equal to {centimetres}cm")

def choicelogic(user_choice):
    if user_choice == "I" or "i":
        return inches_to_centimetres()
    if user_choice == "C" or "c":
        return centimetres_to_inches()
    else:
        return main()

def main():
    user_choice = str(input("Inputting Inches or Centimetres (I/C)? : "))
    return choicelogic(user_choice)
    
main()