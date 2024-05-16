import uuid
from time import sleep
from fx_ef import context
import json

x = 1

while True:

    print("testing SECRETs functionality", flush=True)
    # test_secret = context.secrets.get("testsecret")
    # print(test_secret)

    test_secret_set = context.secrets.set("recentsecret", json.dumps({"value": "testy"}), "project")
    print(test_secret_set)

    x += 1
    sleep(5)
    break

