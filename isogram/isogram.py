"""
    this program returns True if it is an isogram or False if it is not
"""

def is_isogram(word):
    #keep track of the current word
    result = ''
    #loop through the string
    for c in word:
        if c not in result:
            result += c
        else:
            return False
    return True

print is_isogram("background")
print is_isogram("eleven")
