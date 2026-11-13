def calculate_total(price, number):
    total = price * number
    return total
def calculate_discount(total):
    num2 = total * 0.9
    return num2
def shopping(price, number):
    x=calculate_total(price, number)
    y=calculate_discount(x)
    return y
i=shopping(40,4)
print(i)
