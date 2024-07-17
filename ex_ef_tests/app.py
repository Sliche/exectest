import uuid
from time import sleep
from fx_ef import context


def not_working_msg(entity):
    print(entity + " not working properly")


print("testing STORAGE functionality", flush=True)
try:
    with open("/tmp/testfiles.txt", "w") as file:
        file.write("test value")
        file.close()
    file = open("/tmp/testfiles.txt", 'rb')
    bucket_name = "ctxbucket"

    try:
        bucket = context.storage.create_bucket(bucket_name)
    except Exception as e:
        print("Bucket " + bucket_name + " already exists.")

    upload_file = context.storage.upload(bucket_name, file)
    download_file = context.storage.download("testfiles.txt", "file", "/tmp/testfile.txt")
    print(download_file, flush=True)
    print("STORAGE working properly")
except Exception as e:
    not_working_msg("STORAGE")

sleep(1)

print("testing STATE functionality", flush=True)
try:
    test_state_set = context.state.put("testkey", "testval")
    test_state = context.state.get()
    print(test_state, flush=True)
except Exception as e:
    not_working_msg("STATE")

sleep(1)


print("testing SECRETS functionality", flush=True)
try:
    test_secret = context.secrets.get("recentsecret")
    print(test_secret)
    test_secret_set = context.secrets.set("recentsecret", {"value": "testy"}, "project")
    print(test_secret_set)
except Exception as e:
    not_working_msg("SECRETS")

sleep(1)

print("testing EXEC RESULTS functionality", flush=True)
try:
    context.result.save({"my_result": "saved"})

except Exception as e:
    not_working_msg("EXEC RESULTS")

sleep(1)

print("testing EVENTS functionality", flush=True)
try:
    context.events.send("event_type_test", "event_source_my_package", data={"test1": "test2"},
                        reference_id="ref_id_test")
except Exception as e:
    not_working_msg("EVENTS")


