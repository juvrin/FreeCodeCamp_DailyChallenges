def dive(map, coordinates):
    checkcor = map[coordinates[0]][coordinates[1]]
    check_unrecovered = 0
    for i in map:
        for j in i:
            if j == "O":
                check_unrecovered += 1


    if checkcor == "-":
        result = "Empty" 
    elif checkcor == "O" and check_unrecovered == 1:
        result = "Recovered"
    else:
        result = "Found"
    return result

test = dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) 
print(test)

