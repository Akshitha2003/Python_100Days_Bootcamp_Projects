# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as letter_template:
    letter = letter_template.read()

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name.strip("\n")}.txt", mode="w") as file:
        file.write(letter.replace("[name]", name))

    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp