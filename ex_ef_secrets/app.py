import uuid
from time import sleep
from fx_ef import context
import json

x = 1

while True:

    print("testing SECRETs functionality", flush=True)
    test_secret = context.secrets.get("recentsecret")
    print(test_secret)

    test_secret_set = context.secrets.set("recentsecret", {"value": "testy"}, "project")
    print(test_secret_set)

    # x += 1
    # sleep(5)
    break

