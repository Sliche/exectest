import uuid
from time import sleep
from fx_ef import context

x = 1

while True:

    print("testing STATE functionality", flush=True)
    test_state_set = context.state.put("testkey", "testval")
    test_state = context.state.get()
    print(test_state, flush=True)

    x += 1
    sleep(5)
    break
