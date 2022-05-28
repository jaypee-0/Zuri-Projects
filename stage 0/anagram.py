def find_anagrams(word, anagram):
    if list(word)!= list(anagram):
        return False
        
    word =  sorted(word)
    anagram = sorted(anagram)
    for i in range(len(word)-1):
        if word[i]!=anagram[i]:
            return False

    return True

print(find_anagrams('below','below'))  ## Returns True
print(find_anagrams("hello", "check")) ## Returns Falsee