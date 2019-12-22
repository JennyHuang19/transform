'''
Created on Feb 26, 2018

@author: ola
'''
# What is the conceptual difference between Vowelizer.encrypt and Vowelizer.decrypt?
# encrypt takes 1 word and removes the vowels. Decrypt gets a string with no vowels and randomly matches it onto a possible word that the noVowels could be.
# 
# Which of the Vowelizer.encrypt and Vowelizer.decrypt functions runs more quickly and why?
# Vowelizer.encrypt?
#
# When is the value NT_WORD returned by Vowelizer.decrypt?
# When decrypt cannot find a possible voweled-word that would yield word. 
#
# How is Vowelizer.encrypt called from the Transform.py module?
# doTransform("-nvw", Vowelizer.encrypt) in the main block. "doTransform(suffix, transform):"

# When does decrypt(encrypt(w)) == w, i.e., for what words w does this happen?
# it happens to choose the original word.

from pathlib import Path
lowerwords = []
novowels = []

def isVowel(ch):
    """
    Return True if ch is a vowel and False otherwise
    """
    return "aeiouAEIOU".count(ch) > 0

def encrypt(word):
    """
    Return a string that is word
    with all vowels removed, other letters/chars
    in original order as in word
    """
    nv = [ch for ch in word if not isVowel(ch)]
    return ''.join(nv)

def loadlower(): #creating all the words in a file
    """
    Set global variables so that 
    lowerwords is all the words from a file of words
    and novowels is the list of these words with
    all vowels removed. This means that
    novowels[k] is the encrypted form of lowerwords[k]
    
    Returns the 
    """
    global lowerwords, novowels
    f = open(str(Path("data", "lowerwords.txt")))
    lowerwords = [w.strip() for w in f.read().split()]
    novowels = [encrypt(w) for w in lowerwords] #punctuation not removed.
    f.close()
    return lowerwords

def decrypt(word):
    """
    String word has no vowels
    Find a match for word formed
    by finding a word that could have vowels
    removed to yield word. If more than one
    such word, choose one. If no such word found
    then return "NT_WORD"
    
    Note: this code depends on global variables
    lowerwords and novowels. These are initialized
    once and then the values used on all other calls 
    after initialization
    """
    global lowerwords, novowels
    if len(lowerwords) == 0: #empty lst
        lowerwords = loadlower() #fills lst with all words in file
        print("read words in Vowelizer")
    
    word = word.lower() #lowecases all the words
    matches = [dex for dex in range(len(novowels)) if novowels[dex] == word] #fills a list of indexes of the word.
    #print("%d number of matches for %s" % (len(matches),word))
    if len(matches) > 0:
        return lowerwords[matches[0]] #returns the 
    return "NT_WORD"
    

if __name__ == '__main__':
    words = ["vowels", "strength", "oasis", "elephant"]
    ewords = []
    for w in words:
        ew = encrypt(w)
        ewords.append(ew)
        print(w,ew)
    
    print("decrypting")
    for w in ewords:
        dw = decrypt(w)
        print(w,dw)
