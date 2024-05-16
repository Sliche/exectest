import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing SECRETs functionality", flush=True)
    # test_secret = context.secrets.get("testsecret")
    # print(test_secret)

    test_secret_set = context.secrets.set("recentsecret", "value", "context")
    print(test_secret_set)

    x += 1
    sleep(5)
    break

