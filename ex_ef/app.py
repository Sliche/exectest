from time import sleep

x = 1

while True:

    print(x)
    x += 1
    sleep(1)
    if x == 100:
        break
