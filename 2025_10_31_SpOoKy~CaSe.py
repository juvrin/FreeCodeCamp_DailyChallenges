def spookify(boo):
    replacements = str.maketrans({"-": "~", "_": "~"})
    res = boo.translate(replacements).capitalize()
    i = True
    result = ""
    for char in res:
        if i:
            result += char.upper()
        else:
            result += char.lower()
        if char != " " and char != "~" :
            i = not i
    return result

test = spookify("Hello_World")
print(test)