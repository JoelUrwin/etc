user_input = str(input("Enter :").lower())
processed_input = user_input.split()

for i, word in enumerate(processed_input):


    if word[0] in 'aeiou':
        processed_input[i] = processed_input[i] + "ay"
    else:
        
        vowel = False

        for j, char in enumerate(processed_input):
            if char in 'aeiou':
                processed_input[i] = word[j:] + word[:j] + "ay"
                vowel = True
                break

        if vowel == False:
            processed_input[i] = processed_input[i] + "ay"


translated_to_piglatin = ' '.join(processed_input)
print(f"Input : {user_input}")
print(f"Output (Translated) : {processed_input}")