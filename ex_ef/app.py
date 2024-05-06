import uuid
from time import sleep
from fx_ef import context

x = 1

while True:


    bora_sec = context.secrets.get("bora")
    print(bora_sec, flush=True)
    bora_set = context.secrets.set("borasec", "value", "context")

    bora_state = context.state.get()
    print(bora_state, flush=True)



    # bora_state_set = context.state.put("boretinax", "koretinax")

    # context.storage.create_bucket("borabucka")
    # print("-" * 50)
    # print("borka korka 1")
    # print(context.config)
    # print(context.configs)
    # print(context.params)
    # print(context.package)
    # print("borka korka 2")
    # print("-"*50)
    #
    # my_result_log = {
    #     "result1": "somerka",
    #     "result2": "somerka2",
    #     "result3": "somerka3",
    #     "result4": "jugoslovenka"
    # }


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
