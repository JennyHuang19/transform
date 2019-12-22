'''
Created on Oct 21, 2019

@author: Jenny Huang
'''
from pathlib import Path
shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3] #shifted alphabet
shifted_upper = upper_alph[3:] + upper_alph[:3]
import os.path


def encrypt(word):
    """
    Changes a word into its Caesar-ciphered form.
    """ 
    newWord = ""
    #go through all the characters in a word.
    for ch in word:
        if ch in lower_alph:
    #find where the character is in lower_alph
            ind = lower_alph.index(ch)
    #use this index to find the encrypted character
            newLetter = shifted_lower[ind]
    #create a new string joining encrypted ch
            newWord += newLetter
        elif ch in upper_alph:
            ind = upper_alph.index(ch)
            newLetter = shifted_upper[ind]
            newWord += newLetter
        else:
            newLetter = ch 
            newWord += newLetter
    return newWord

def setShift(n):
    """
    Sets the values of the three global variables shift, shifted_lower,
    and shifted_upper so that shift is the value (n) that the alphabet is 
    shifted to the right by, and shift_upper/shift_lower is the entire
    alphabet starting with the letter corresponding to n.  
    """ 
    global shift, shifted_lower, shifted_upper
    shift = n
    shifted_lower = lower_alph[n:] + lower_alph[:n]
    shifted_upper = upper_alph[n:] + upper_alph[:n]

    
def findShift(st):
    """
    Finds the "key", the number that the
    alphabet was shifted by to result
    in a certain string output.
    """
    sh = -1 #a list of indexes 
    Encrypted = [] #a list of strings that are encrypted with index sh
    
    numReal = 0
    #the set of real words read from lowerwords.txt in Step 1
    import os.path
    file = os.path.join("data","lowerwords.txt")
    f = open(file)
    #put all of the real words in a list
    wordsClean = [w.strip() for w in f.read().split()]
    f.close()
    #call setShift for all 26 possible shifts (0-25), to output 26 possible decrypted words.
    for i in range(26):
        setShift(i)
        wordsDecrypt = [encrypt(w) for w in st.split()]
    #For each shift in wordsDecrypt, find out how many of the decrypted strings are real words.
        realWords = len(set(wordsClean)&set(wordsDecrypt))
        if realWords > numReal:
            sh = i #retrieves index that gave largest realWords
            numReal = realWords
            
    #return the shift that yields the largest intersection between wordsClean and wordsDecrypt
    return 26 - sh 

    
    
if __name__ == '__main__':
    #setShift(1)
    words = ["vowels", "strength", "oasis", "elephant"]
    ewords = []
    for w in words:
        ew = encrypt(w)
        ewords.append(ew)
        print(w,ew)
     
#     print(findShift("Bxvncrvnb rc'b njbh cx lxdwc oaxv 1-10, kdc wxc jufjhb"))
        
#     setShift(10)
#     ew = encrypt("zebra")
#     setShift(16)
#     w = encrypt(ew)
#     print(ew,w)
    

    