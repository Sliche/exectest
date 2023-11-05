from time import sleep
from fx_ef import context

x = 1

while True:

    print("-" * 50)
    print(x)
    context.logging.debug("debug msg")
    context.logging.info("info msg")
    context.logging.error("error msg")
    context.logging.warning("warning msg")
    context.logging.critical("critical msg")
    print("-"*50)

    x += 1
    sleep(1)

    if x == 100:
        break
