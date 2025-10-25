def to_decimal(binary):
    result = 0
    i = 0
    for b in reversed(binary):   
        result += int(b) * pow(2,i)
        i += 1       
    return result


# to_decimal("101") should return 5.
test = to_decimal("101")
print(test)