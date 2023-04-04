import time
# your code goes here!
def countdown(number):
    i = number
    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    i = number
    while i >0:
        print(f'{i} SECOND(S)!')
        time.sleep(1)
        i -= 1
    print("HAPPY NEW YEAR!")