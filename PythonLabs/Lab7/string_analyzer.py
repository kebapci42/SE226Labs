import string_package as sp

sent = input("Give me some words:")

print("The reversed version of what you've written is:\n" + sp.reverse_string(sent))
print("\nThe capitalized version of what you've written is:\n" + sp.capitalize_words(sent))
print("\nThe version without punctuations of what you've written is:\n" + sp.remove_punctuations(sent))
print("\nThe number of characters of what you've written is:\n" + sp.count_characters(sent))
print("\nThe number of words of what you've written is:\n" + sp.count_words(sent))
print("\nThe average word length of what you've written is:\n" + sp.average_word_length(sent))