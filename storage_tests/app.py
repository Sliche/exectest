import uuid
from time import sleep
from fx_ef import context



context.storage.create_bucket("borabucka")

print("-" * 50)
print("borka korka 1")
print("-"*50)

my_result_log = {
    "result1": "somerka",
    "result2": "somerka2",
    "result3": "somerka3",
    "result4": "jugoslovenka"
}

