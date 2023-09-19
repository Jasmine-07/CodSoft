import random
import string

def password_generator(minlength,numbers= True, special_characters= True):#we'll see what the user wants to be included in the password such as numbers or special characters etc.
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    character = letters
    if numbers:
        character += digits
    if special_characters:
        character += special
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < minlength:
        new_char = random.choice(character)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special   

    return password   

password= password_generator(10) #generates the password according to the length specified, for example in this case 10
print(password)
#Password will be a combination of new and unique characters and digits everytime the user will ask for the password. Thids will help in keeping the authenticity of the password 
