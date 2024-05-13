import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing STORAGE PRESIGN functionality", flush=True)

    presigned_url = context.storage.get_public_url("buckettest", "file", 5)

    print(presigned_url, flush=True)

    x += 1
    sleep(5)
    break

