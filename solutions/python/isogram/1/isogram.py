def is_isogram(phrase):
    phrase = phrase.lower()
    phrase = "".join(char for char in phrase if char.isalnum())
    return len(set(phrase)) == len(phrase)
