'''
Created on Oct 23, 2019

@author: JennyH
'''

lowerwords = [] #all the words from a file of words
piglatin = [] #encrypted lowerwords
vowels = "AEIOUaeiou"
vowelsy = "AEIOUYaeiouy"
vowelsnou = "AEIOYaeioy"


#helper functions
def beginsWithVowel(word):
    """
    Returns pig-latin for words that begin with vowels
    """
    return word + "-way"
    print(beginsWithVowel("umbrella"))
    
def beginsConsonant(word):
    """
    Returns pig-latin for words that begin with consonants
    """
    vowels = "AEIOUaeiou"
    for ch in word:
        if ch in vowels:
            ind = word.index(ch)
            break #stops after finding first vowel
        else:
            ind = 0
    return word[ind:] + "-" + word[:ind] + "ay"
    
def beginsQu(word):
    """
    Returns pig-latin for words that begin with "qu/Qu"
    """
    global vowels
    vowels = "AEIOaeio"
    for ch in word:
        if ch in vowels:
            ind = word.index(ch)
            break #stops after finding first vowel 
    return word[ind:] + "-" + word[:ind] + "ay"

def beginsWithY(word):
    """
    Returns pig-latin for words that begin with "Y/y"
    """
    global vowels
    vowels = "AEIOUaeiou"
    for ch in word:
        if ch in vowels:
            ind = word.index(ch)
            break #stops after finding first vowel
    return word[ind:] + "-" + word[:ind] + "ay"

    
def noVowels(word):
    """
    Returns pig-latin for words that do not contain vowels.
    """
    return word[:] + "-" + "way"

def isYVowel(word):
    #y acts as a vowel if there are no other vowels.


#helper functions for conditional statements
    def containsOnlyConsonants(word):
        """ 
        checks for words that contain only consonants
        """
        for i in word:
            if i in vowels:
                c = False
            else:
                c = True
        return c

def beginsWithConsonant(word):
    """
    checks for words that begin with consonants.
    """
    for i in word:
        if i[0] in vowels:
            return False
        else:
            return True
        

        
def encryptWord(word):
    """
    Changes a word to its pig-latin form.
    """
      
    if word[0] in vowels:
        encWord = beginsWithVowel(word)
    
    if word[0] not in vowels:
        encWord = beginsConsonant(word)
    
#     if containsOnlyConsonants(word):
#         encWord = noVowels(word)
        
    if vowels not in word:
        if "y" or "Y" in word: #change y to a vowel
            ind = word.index("y")
            encword = word[ind:] + "-" + word[:ind] + "ay"
        else:
            encWord = noVowels(word)
        
    if word[0].lower() == "y":
        encWord = beginsWithY(word)
        
    if word[:2].lower() == "qu": #specific cases last
       encWord = beginsQu(word)
    
    
    return encWord 

def encrypt(phrase):
    """
    Encrypts a list of words,
    then joins into a string.
    """
    ret = []
    lst = phrase.split()
    for w in lst:
        ret.append(encryptWord(w))
    return "".join(ret)
 

if __name__ == '__main__':
    pass