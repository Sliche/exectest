import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    # print("testing SECRETs functionality", flush=True)
    # bora_sec = context.secrets.get("testsecret")
    # bora_set = context.secrets.set("testsecret", "value", "context")

    # print("testing STATE functionality", flush=True)
    # test_state_set = context.state.put("testkey", "testval")
    # test_state = context.state.get()
    # print(test_state, flush=True)

    # print("testing EVENTS functionality", flush=True)
    # context.events.send("event_type_test", "event_source_my_package", data={"test1":"test2"}, topic="ferris.events", reference_id="ref_id_test")


    print("testing EXEC RESULTS functionality", flush=True)
    context.result.save({"my_result": "saved"})

    x += 1
    sleep(5)
    break

    # if x == 100:
    #     break
