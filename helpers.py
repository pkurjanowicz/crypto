def alphabet_position(letter):
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter in alphabet:
        return alphabet.index(letter)
