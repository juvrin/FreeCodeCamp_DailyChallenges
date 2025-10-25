#https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-02
#hier gevonden hoe je dat moet doen https://gristle.tripod.com/hexconv.html




def rgb_to_hex(rgb):
    string_strip = rgb.replace("rgb(", "")
    string_strip = string_strip.replace(")", "")
    string_split = string_strip.split(",")

    rgb = "#"
    for num in string_split:
        number = int(num)

        #integer division
        div = number // 16
        #check remainder with modulo
        remainder = number % 16
        num_to_let = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}

        if div >=10:
            div = num_to_let.get(div, "")
        if remainder >= 10:
            remainder = num_to_let.get(remainder, "")
        rgb += f"{div}{remainder}"
    
    return rgb
        

output = rgb_to_hex("rgb(173, 216, 230)")
print(output)