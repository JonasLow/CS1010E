def calc_poly(const_seq, var_poly):
    total_sum = 0
    order = 0
    i = 0
    while True:
        try:
            while i < len(const_seq):
                if const_seq[i] == "-":
                    total_sum += (float(const_seq[i] + const_seq[i + 1]) * var_poly ** order)
                    order += 1
                    i += 2
                else:
                    total_sum += (float(const_seq[i]) * var_poly ** order)
                    order += 1
                    i += 1
            if (total_sum % 1 == 0):
                return int(total_sum)
            else:
                return round(total_sum, 2)
        
        except (TypeError, ValueError):
            i += 1
            pass

def main():
    seq = input("const_seq = ")
    var = float(input("var_poly = "))
    result = calc_poly(seq, var)
    print(result)

if __name__== "__main__":
    main()
