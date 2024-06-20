import random
import string

def generate_password(length, use_numbers=True, use_special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    characters = letters
    if use_numbers:
        characters += digits
    if use_special_characters:
        characters += special_chars
    
    password = ""
    is_valid = False
    contains_number = False
    contains_special_char = False
    
    while not is_valid or len(password) < length:
        new_char = random.choice(characters)
        password += new_char
        
        if new_char in digits:
            contains_number = True
        if new_char in special_chars:
            contains_special_char = True
        
        is_valid = True
        if use_numbers:
            is_valid = contains_number
        if use_special_characters:
            is_valid = is_valid and contains_special_char
    
    return password


min_length = int(input("Enter minimum length: "))
include_numbers = input("Include numbers (1/0): ").lower() == "1"
include_special_chars = input("Include special characters (1/0): ").lower() == "1"

generated_password = generate_password(min_length, include_numbers, include_special_chars)
print("Generated password:", generated_password)