'''
Input : a string (actually a phrase containing words seperated by whitespaces)
Output : a string (a new phrase containing all the words from the old phrase, in a ordered way)
Keep in mind that we don't care about the case
'''

def sort_words(phrase):
    words = phrase.split()
    # [banana ORANGE apple]
    words = [w.lower() + w for w in words]
    # [bananabanana orangeORANGE appleapple]
    words.sort()
    # [appleapple bananabanana orangeORANGE]
    words = [w[len(w)//2:] for w in words]
    # [apple banana ORANGE]
    return ' '.join(words)