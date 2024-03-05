import uuid
from time import sleep
from fx_ef import context


print("uploading file")
# context.storage.create_bucket("borabucka")
context.storage.upload("borabucka", "/app/launch.sh")
print("file uploaded ")

print("-" * 50)
print("borka korka 1")
print("-"*50)

# my_result_log = {
#     "result1": "somerka",
#     "result2": "somerka2",
#     "result3": "somerka3",
#     "result4": "jugoslovenka"
# }

