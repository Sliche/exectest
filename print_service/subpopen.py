import subprocess
import sys
from threading import Timer

# def redirect_output():
#     import sys, os
#     # The opened file needs to stay alive
#     redirect_output._file = open('/tmp/logfile.log', 'w')
#
#     os.dup2(redirect_output._file.fileno(), sys.stdout.fileno())

# subp_script_res = subprocess.Popen(
#             ['python3', 'app.py'],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.STDOUT,
#             # timeout=5,
#             # preexec_fn=redirect_output
#         )

logfile = open('/tmp/logs/logfile.log', 'w')
logfile_err = open('/tmp/logs/errfile.log', 'w')

subp_script_res = subprocess.Popen(
            ['python3', 'app.py'],
            stdout=logfile,
            stderr=logfile_err,
            bufsize=1,
            universal_newlines=True
            # timeout=5,
            # preexec_fn=redirect_output
        )

subp_script_res.wait()

# some_file = open('/tmp/logs/logfile.log', 'r')
lines = logfile.readlines()

print(lines)

# print(logfile.read())
# print(logfile_err.read())


if subp_script_res.returncode == 0:
    print("Subprocess completed successfully.")
else:
    print(f"Subprocess exited with an error code: {subp_script_res.returncode}")

std_out = subp_script_res.stdout
std_err = subp_script_res.stderr

timer = Timer(20, subp_script_res.kill)
timer.start()
timer.cancel()

print(timer.is_alive())
print("done")
