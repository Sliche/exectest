import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing EVENTS functionality", flush=True)
    hash_key = b'P38lbYCl11RzNtYcLIlnGxTx2i5ldYbtoJCVcraOe7I='
    context.events.send("event_type_test", "event_source_my_package", data={"test1":"test2"}, reference_id="ref_id_test", hash_key=hash_key)

    x += 1
    sleep(5)
    break
