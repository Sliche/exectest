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

    context.events.send(
        event_type="ferris_executor.save_users_logs",
        data={
            "fxcid": str(uuid.uuid4()),
            "log_content": "borkica",
            "last_log": False
        }
    )

    x += 1
    sleep(5)

    if x == 100:
        break
