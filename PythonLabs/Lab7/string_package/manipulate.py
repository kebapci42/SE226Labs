import string


def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.upper()

def remove_punctuations(s):
    for char in string.punctuation:
        s = s.replace(char, "")
    return s