def print_upper_words(words):
    """print out each word on a separate line, but in all uppercase"""

    for word in words:
      print(word.upper())

def print_word_start_with(words):
    """prints words that start with the letter ‘e’ (either upper or lowercase)"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_word_start_with1(words, must_start_with):
    """ prints words that start with one of those letters."""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper)





