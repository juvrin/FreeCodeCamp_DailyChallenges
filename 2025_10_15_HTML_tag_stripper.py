def strip_tags(html):
    opentags = []
    closetags= []
    stripped = []
    for i in range(len(html)):
        if html[i] == "<":
            opentags.append(i)
        if html[i] == ">":
            closetags.append(i)

    for i in range(1, len(closetags)):
        stripped.append(html[closetags[i-1]+1:opentags[i]])
    result = ''.join(stripped)

    return result


test = strip_tags('<a href="#">Click here</a>')
# # should return "Click here"
print(test)

test2 = strip_tags('<p class="center">Hello <b>World</b>!</p>') 
# should return "Hello World!"
print(test2)


# with regular expressions, ook een optie, maar ik kwam er niet uit
# import re

# #ik was al een eindje met het bouwen van een regex
# # # (<(p|b|img|main|a)\s.+>([a-zA-Z0-9_]+)</(p|b|img|main|a)>)+
# test3 = '<p class="center">Hello <b>World</b>!</p>'
# print(re.findall("<.+>", test3))
# print(re.split("<.+>", test3))
# print(re.sub("<.+>", "DOG", test3))

# if re.search("<.+>", test3):
#     print("Valid")
# else:
#     print("Invalid")


# def main():
#     print(parse(input("HTML: ")))

# def parse(s):
#     matches = re.match(r"^(<iframe)(.+)(src=\")(http)(?:s?)(://)(www\.)?(youtube.com/embed/)([a-zA-Z0-9_]+)(.+)(</iframe>)$",s)

#     if matches:
#         if matches.group(7) == "youtube.com/embed/":
#             short_url = f"https://youtu.be/{matches.group(8)}"
#             return short_url
#         else:
#             return None
#     else:
#         return None


# if __name__ == "__main__":
#     main()
    

