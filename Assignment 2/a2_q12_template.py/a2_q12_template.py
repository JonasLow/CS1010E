# count_substring(string) should return the number of substrings that begin with character 'A' and ends with character 'X'
# Can assume that string is composed of upper case letters only

def count_substring(string):
    i = 0
    n = i
    count = 0
    while i < len(string):
        if (string[i] == 'A' and string[n] == 'X'):
            count += 1
            n += 1
        elif (string[i] == 'A' and n < (len(string) - 1)):
            n += 1
        else:
            i += 1
            n = i
    
    return count
