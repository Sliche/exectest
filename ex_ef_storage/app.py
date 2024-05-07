import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing STORAGE functionality", flush=True)

    with open("/tmp/testfiles.txt", "w") as file:
        file.write("test value")

    bora_set = context.storage.upload("buckettest", file)

    x += 1
    sleep(5)
    break

