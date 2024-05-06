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

    print("testing EVENTS functionality", flush=True)
    context.events.send("event_type_test", "event_source_my_package", data={"test1":"test2"}, topic="testytopic", reference_id="ref_id_test")


    # context.result.save(my_result_log)

    # context.events.send(
    #     event_type="ferris_executor.save_users_logs",
    #     data={
    #         "fxcid": "9ccdac99-ce50-4336-a9c4-ce63d18484ef",
    #         "package_name": context.params["package_name"],
    #         "result": my_result_log,
    #         "last_log": False
    #     }
    # )

    # context.output.log("My Custom made logs")
    # context.output.log("My Custom made logs")
    # context.output.log("My Custom made logs")
    # context.output.log("My Custom made logs", last_log=True)

    x += 1
    sleep(5)
    break

    # if x == 100:
    #     break
