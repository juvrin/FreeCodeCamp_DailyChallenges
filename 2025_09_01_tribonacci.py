#https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-01

def tribonacci_sequence(start_sequence, length):
    tribonacci= []
    
    if length > 2:
        tribonacci = start_sequence
        for i in range(2, length-1):
            sum = tribonacci[i-2] + tribonacci[i-1] + tribonacci[i]
            tribonacci.append(sum)
    elif length == 2:
        tribonacci.append(start_sequence[0])
        tribonacci.append(start_sequence[1])
    elif length == 1:
        tribonacci.append(start_sequence[0])
    elif length == 0:
        tribonacci = []

    return tribonacci

ding = tribonacci_sequence([21, 32, 43], 1)
print(ding)
print(len(ding))
