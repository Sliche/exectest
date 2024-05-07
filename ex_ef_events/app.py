import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing EVENTS functionality", flush=True)
    context.events.send("event_type_test", "event_source_my_package", data={"test1":"test2"}, topic="ferris.events", reference_id="ref_id_test")

    x += 1
    sleep(5)
    break
