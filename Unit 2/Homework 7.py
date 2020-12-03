year = {

    "January": 31,
    "February": "28/29",
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October":31,
    "November":30,
    "December": 31

}

months = [ "January", "February", "March", "April", "May", "June", "July", "August" , "September", "October", "November", "December"]

#Dictionary contains all the days that are in a month, this makes it easier to reference when looking for the amount of days.
#Months is a list that will be used to compare the user input with.

def userinput():
    x = str(input("Input Month: "))
    return x
    #requests user's input of month, returns the value that is entered

def main():
    user_input = userinput()
    if user_input not in months:
        userinput()
        #restarts if the input is not a month or is not properly entered
    if user_input in months:
        #outputs the amount of days from the dictionary and the month.
        #uses fstrings to achieve this.
        return print(f"There are {year[user_input]} Days in {user_input}.")
    else:
        userinput()
    
main()
#starts the main function of the program