# import time
# import logging
# print("Boracar")
# print("newprint")
#
# for i in range(10):
#     print("waiting " + str(i) + " seconds", flush=True)
#     # x = a + b
#     time.sleep(1)
#
# # print(boretina)


import logging
from ferris_ef import context
from time import sleep


context.logging.debug({"debug msg": "ddddd"})
context.logging.info(['info msg', "dasfdasdfas"])
context.logging.error(context)
context.logging.warning(['info msg', "dasfdasdfas"])
context.logging.critical({"debug msg": "ddddd"})


for i in range(1, 100):
    for j in range(0, i):
        context.logging.debug(f"log line {i} {j}")
    sleep(1)

