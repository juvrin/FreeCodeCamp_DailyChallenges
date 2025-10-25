def adjust_thermostat(current_f, target_c):
    target_f =  (target_c * 1.8) + 32
    diff = current_f - target_f
    if diff == 0:
        result = "Hold"
    if diff < 0:
        result = f"Heat: {round(abs(diff),1)} degrees Fahrenheit"
    if diff > 0:
        result = f"Cool: {round(abs(diff),1)} degrees Fahrenheit"
    return result

test = adjust_thermostat(72, 18) 
print(test)