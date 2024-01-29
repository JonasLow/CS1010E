def get_price(num_of_items):
    price = 0
    item = [10, 8, 6, 1]
    cost = [4.70, 3.80, 2.90, 0.50]
    for i in range(4):
        n = num_of_items // item[i]
        if n != 0:
            price += n * cost[i]
        num_of_items -= n * item[i]
        i += 1
    return price

print(get_price(4))
print(get_price(20))
print(get_price(17))
