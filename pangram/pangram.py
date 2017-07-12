"""
    get a list of ascii letters, make sure the word is in all lower case using
"""
import string

def is_pangram(phrase):
    #store a list of ascii letters in all lowercase
    alphabet = string.ascii_lowercase
    alphabet = set(alphabet)
    #make sure the phrase is lower / it is not case sensitive
    phrase = set(phrase.lower())
    #compare the set to the phrase we received
    return alphabet <= phrase

print is_pangram("the cow jumped over the moon")

print is_pangram("the quick brown fox jumps over the lazy dog")

print is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog")
