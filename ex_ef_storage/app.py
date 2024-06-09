import uuid
from time import sleep
from fx_ef import context

x = 1


print("testing STORAGE functionality", flush=True)

with open("/tmp/testfiles.txt", "w") as file:
    file.write("test value")
    file.close()

file = open("/tmp/testfiles.txt", 'rb')

bucket_name = "ctxbucket"

try:
    bucket = context.storage.create_bucket(bucket_name)
except Exception as e:
    print("Bucket " + bucket_name + " already exists.")

upload_file = context.storage.upload(bucket_name, file)
download_file = context.storage.download("buckettest", "file", "/tmp")

print(download_file, flush=True)

sleep(2)

