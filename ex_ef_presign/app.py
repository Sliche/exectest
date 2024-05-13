import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing STORAGE PRESIGN functionality", flush=True)

    upload_file = context.storage.get_public_url("buckettest", file)


    print(download_file, flush=True)

    x += 1
    sleep(5)
    break

