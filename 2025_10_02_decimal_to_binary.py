def to_binary(decimal):

    remainders = ""
    startnum = decimal

    while startnum != 0:
        startnum = decimal // 2
        remainder = decimal % 2
        remainders += str(remainder)
        decimal = startnum
    s = remainders[::-1]
    return s

x= to_binary(5)
print(x)