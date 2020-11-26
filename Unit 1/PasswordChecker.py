import string
user_input = input("Password :")


def lengthCheck(a_str):
    if len(a_str) < 8:
        return False
    return True
    

def upperCaseCheck(a_str):
    for c in a_str:
        if c not in string.ascii_uppercase:
            continue
        if c in string.ascii_uppercase:
            return True

        print("failed uppercase check")
        return False
        

def lowerCaseCheck(a_str):
    for c in a_str:
        if c not in string.ascii_lowercase:
            continue
        if c in string.ascii_lowercase:
            return True
            
        print("failed lowercase check")
        return False
        

def numberCaseCheck(a_str):
    for c in a_str:
        if c.isdigit() == False:
            continue
        if c.isdigit() == True:
            return True
        print("Failed Number Case Check")
        return True
        

def passwordLogic(x):
    PasswordLengthCheckPass = lengthCheck(x)
    PasswordCapsCheckPass = upperCaseCheck(x)
    PasswordLowerCheckPass = lowerCaseCheck(x)
    PasswordNumCheckPass = numberCaseCheck(x)

    if PasswordLengthCheckPass == True:
        if PasswordCapsCheckPass == True:
            if PasswordLowerCheckPass == True:
                if PasswordNumCheckPass == True:
                    return print("PASSED THE TEST.")
                return print("Did not contain a number.")
            return print("Did not contain any lower case characters.")
        return print("Did not contain any capital case characters.")
    return print("Password was not longer than 8 characters.")
    
passwordLogic(x=user_input)
