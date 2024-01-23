def triangle(len1, len2, len3):
    if (len1 > len2 + len3 or len2 > len1 + len3 or len3 > len1 + len2):
        return "Not a triangle"
    elif (len1 == len2 == len3):
        return "Equilateral"
    elif ((len1 == len2 and len2 != len3) or (len1 != len2 and len2 == len3) or (len1 == len3 and len1 != len2)):
        return "Isosceles"
    else:
        return "Scalene"
    
print(triangle(5,3,3))