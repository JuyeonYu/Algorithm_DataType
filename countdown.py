def countdown_while(num):
    while num > 0:
        print(num)
        num = num -1

def countdown_self(num):
    print(num)
    if num > 1:
        countdown_self(num-1)