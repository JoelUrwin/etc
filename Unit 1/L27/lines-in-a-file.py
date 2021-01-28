file_path = input("Enter File Path : ")

count = len(open(file_path).readlines(  ))

print(f"There are {count} lines in this file.")
