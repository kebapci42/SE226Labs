def count_characters(s):
    return str(len(s))

def count_words(s):
    temp = s.split()
    return str(len(temp))

def average_word_length(s):
    temp = s.split()
    res = 0
    
    for word in temp:
        res += len(word)
    
    return str(float(res) / len(temp))