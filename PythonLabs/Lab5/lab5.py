import random
import string

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)



letters_and_replacements = {}
used_replacements = set()
for i in range(5):
    letter = input("Please, enter a lowercase character: ").lower()
    
    replacements = set()
    for _ in range(3):
        repl_char = input(f"Please, enter a replacement for '{letter}': ")
        if repl_char not in used_replacements:
            replacements.add(repl_char)
            used_replacements.add(repl_char)
        else:
            print(f"'{repl_char}' has already been used. Please enter a different character.")
    
    letters_and_replacements[letter] = replacements



categorized_passwords = {}
changed_passwords = []
for password in passwords:
    pword_letters = list(password)
    changed_pword_letters = []
    for lett in pword_letters:
        strength_counter = 0
        if lett in letters_and_replacements.keys():
            if letters_and_replacements[lett]:
                changed_pword_letters.append(random.choice(list(letters_and_replacements[lett])))
                strength_counter += 1
            else:
                changed_pword_letters.append(lett)
        else:
            changed_pword_letters.append(lett)
    
    changed_password = ''.join(changed_pword_letters)
    changed_passwords.append(changed_password)
    
    # Check for strength
    if strength_counter >= 4:
        categorized_passwords[changed_password] = 'strong'
    else:
        categorized_passwords[changed_password] = 'weak'
    
print(passwords)
print(changed_passwords)
print("\nStrong passwords: ")
for password, power in categorized_passwords.items():
    if power == "strong":
        print(password)
        
print("Weak passwords: ")
for password, power in categorized_passwords.items():
    if power == "weak":
        print(password)
