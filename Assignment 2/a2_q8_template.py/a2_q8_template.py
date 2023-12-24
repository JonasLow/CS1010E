def is_anagram(s1, s2):
    # You may assume that s1 and s2 consists of only lowercase or uppercase letters from the English alphabets
    wordbank = {}
    for alphabet in s1:
        if (alphabet not in wordbank):
            wordbank[alphabet] = 1
        else:
            wordbank[alphabet] += 1
    for character in s2:
        if character in wordbank:
            wordbank[character] -= 1
            if wordbank[character] < 0:
                return False
        else:
            return False
        
    for item in wordbank:
        if wordbank[item] > 0:
            return False
        
    return True
