import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing EXEC RESULTS functionality", flush=True)
    context.result.save({"my_result": "saved"})

    x += 1
    sleep(5)
    break
