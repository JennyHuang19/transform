'''
Created on Oct 17, 2019

@author: Jenny Huang
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
    

def beginsWithConsonant(word):
        """
        Returns pig-latin for words that begin with consonants and contain vowels.
        """
        listvowelswithY = []
        for i in word:
            if i in vowelsy: #may have to make vowelsy a list
                listvowelswithY.append(word.index(i)) #list of vowels for qu case
                ind = min(listvowelswithY)
        return word[ind:] + "-" + word[:ind] + "ay"
    
def beginsQu(word):
    """
    Returns pig-latin for words that begin with word[0:2].lower() == "qu"
    """
    listvowelsQu = []
    for i in word:
        if i in vowelsnou: #may have to make vowelsnou a list
            listvowelsQu.append(word.index(i)) #list of vowels for qu case
            ind = min(listvowelsQu)
    return word[ind:] + "-" + "qu" + word[2:ind] + "ay"
            

def beginsWithY(word):
    """
    Returns pig-latin for words that begin with "Y/y"
    """
    return word[1:]+"-yay"

    
def noVowels(word):
    """
    Returns pig-latin for words that do not contain vowels.
    """
    return word[:] + "-" + "way"

        
def encryptWord(word):
    """
    Changes a word to its pig-latin form.
    """
      
    if word[0] in vowels:
        return beginsWithVowel(word)
    else:
        if word[0].lower() == "y":
            return beginsWithY(word)
        if word[:2].lower() == "qu": #specific cases last
            return beginsQu(word)
        countVowel = 0 #a count of the number of vowels in a word
        for i in word:
            if i in vowelsy:
                countVowel +=1
        if countVowel == 0: #for words that don't have vowels
            return beginsWithVowel(word)
            #for words that contain vowels
        if countVowel > 0:
            return beginsWithConsonant(word)
                

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
 



def decryptWord(word):
    """
    Changes a word from pig-latin to English.
    Does this through finding a match for word formed
    by finding a word that could have been encrypted
    to yield word. If more than one
    match, it chooses a word. If no such word
    return "NT_WORD"
    """

    index = word.rfind('-')
    alist = [word[:index], word[index+1:]]
    if alist[1] == 'way':
        return alist[0]
    else:
        answer = word[index+1:-2] + alist[0] #gives the "qu" alist[0] = word
        return answer

def decrypt(phrase):
    """
    Decrypts a list of words then joins 
    into a string.
    """
    ret = []
    lst = phrase.split()
    for w in lst:
        ret.append(decryptWord(w))
    return "".join(ret)
        
    
     
    
if __name__ == '__main__':
    pass
#     print(beginsWithVowel("umbrella"))
#     print(beginsConsonant("string"))
#     print(beginsQu("queue"))
#     print(beginsWithY("yesterday"))
#     print(noVowels("zzz"))
#     
    words = ["yesterday", "strength", "quay", "elephant", "zz"]
    ewords = []
    print("encrypting")
    for w in words:
        ew = encrypt(w)
        ewords.append(ew)
        print(w,ew)
  
    print(beginsWithConsonant("strength"))
#thinks qu is consonant
         
    print("decrypting")
    for w in ewords:
        dw = decrypt(w)
        print(w,dw)  