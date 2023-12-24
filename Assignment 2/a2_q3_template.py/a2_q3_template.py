def at_most_10(txt):
    count = 0
    i = 0
    while count < 11:
        try:
            while i < len(txt):
                x = int(txt[i])
                count += 1
                i += 1
            
            if count < 11:
                return True

        except (TypeError, ValueError):
            pass
            i += 1
    
    return False

