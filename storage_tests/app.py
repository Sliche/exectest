import uuid
from time import sleep
from fx_ef import context


print("downloading file")
# context.storage.create_bucket("borabucka")
# context.storage.upload("borabucka", "launch.dev.sh")
somer = context.storage.download("borabucka", "launch.sh")
print(somer)



