import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing SECRETs functionality", flush=True)
    bora_sec = context.secrets.get("testsecret")
    print(bora_sec)
    print(type(bora_sec))
    # bora_set = context.secrets.set("testsecret", "value", "context")


    x += 1
    sleep(5)
    break

