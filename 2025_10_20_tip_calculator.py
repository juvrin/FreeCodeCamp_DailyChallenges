def calculate_tips(meal_price, custom_tip):
    meal_price = float(meal_price[1:6])
    custom_tip = (int(custom_tip.replace("%","")))/100
    meal_price1 = "$%.2f" % (meal_price*0.15)
    meal_price2 = "$%.2f" % (meal_price*0.2)
    meal_price3 = "$%.2f" % (meal_price*custom_tip)
    result = [meal_price1, meal_price2, meal_price3]
    return result


test = calculate_tips("$19.85", "9%")
print(test)


#result moet ziJN ["$2.98", "$3.97", "$1.79"]