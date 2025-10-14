import time

def countdown(n: int):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        time.sleep(1)
        countdown(n - 1)

countdown(10)
