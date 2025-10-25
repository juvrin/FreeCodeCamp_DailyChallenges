def send_message(route):
    message_time = (sum(route)/300_000) +(len(route)-1)* 0.5
    return round(message_time,4)

test = send_message([54600000, 54600000]) 
print(test)
# should return 364.5


test2 = send_message([10000, 21339, 50000, 31243, 10000]) 
# should return 2.4086
print(test2)
