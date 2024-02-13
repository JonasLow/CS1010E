# count_substring(string) should return the number of substrings that begin with character 'A' and ends with character 'X'
# Can assume that string is composed of upper case letters only

def count_substring(string):
    i = 0
    n = 1
    count = 0
    while n < len(string):
        if (string[i] == 'A' and string[n] == 'X'):
            count += 1
            n += 1
        else:
            n += 1
        if n == len(string) and i < (len(string) - 1):
            i += 1
            n = i + 1
    return count

print(count_substring("AXAXAXAXAX"))
print(count_substring("AAXOXXA"))
print(count_substring("CAXAAYXZA"))
print(count_substring("AAAAXXXX"))
