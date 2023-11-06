from time import sleep
from fx_ef import context

x = 1

while True:

    print("-" * 50)
    print(x)
    print(context.config)
    print(context.configs)
    print("-"*50)

    x += 1
    sleep(1)

    if x == 100:
        break
