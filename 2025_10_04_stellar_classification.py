def classification(temp):

    if temp >= 30000:
        cat = "O"
    elif 10000 <= temp <= 29999:
        cat = "B"
    elif 7500 <= temp <= 9999:
        cat = "A"
    elif 6000 <= temp <= 7499:
        cat = "F"
    elif 5200 <= temp <= 5999:
        cat = "G"
    elif 3700 <= temp <= 5199:
        cat = "K"
    elif 0 <= temp <= 3699:
        cat = "M"
    
    return cat

print(classification(5778))