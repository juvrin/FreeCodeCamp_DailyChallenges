'''
https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-03

A password is evaluated according to the following rules:

    It is at least 8 characters long.
    It contains both uppercase and lowercase letters.
    It contains at least one number.
    It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.

Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
'''
def check_strength(password):
    check1 = 0
    check2 = 0
    check2_upper = 0
    check2_lower = 0
    check3 = 0
    check4 = 0
    spec_char = ["!", "@", "#", "$", "%", "^", "&", "*"]
    if len(password) >= 8:
        check1 = 1
    
    for s in password:
        if s.isupper() == True:
            check2_upper = 1
        if s.islower() == True:
            check2_lower = 1
        if s.isnumeric() == True:
            check3 = 1
        if s in spec_char:
            check4 = 1
    if check2_upper == 1 and check2_lower == 1:
        check2 = 1

    checks = check1 + check2 + check3 +  check4

    if checks < 2:
        password = "weak"
    elif 1< checks < 4:
        password = "medium"
    elif checks == 4:
        password = "strong"

    return password

checks = check_strength("PASSWORD")
print(checks)
