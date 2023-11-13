import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("-" * 50)
    print(x)
    print(context.config)
    print(context.configs)
    print(context.params)
    print(context.package)
    print("-"*50)

    my_result_log = {
        "result1": "somerka",
        "result2": "somerka2",
        "result3": "somerka3",
        "result4": "jugoslovenka"
    }

    context.result.log(my_result_log)

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

    if x == 100:
        break
