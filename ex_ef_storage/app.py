import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing STORAGE functionality", flush=True)

    with open("/tmp/testfiles.txt", "w") as file:
        file.write("test value")
        file.close()

    file = open("/tmp/testfiles.txt", 'rb')

    upload_file = context.storage.upload("buckettest", file)
    # download_file = context.storage.download("buckettest", "file")

    # print(download_file, flush=True)

    x += 1
    sleep(5)
    break

