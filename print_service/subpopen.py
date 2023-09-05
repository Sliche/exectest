import subprocess
import sys

subp_script_res = subprocess.Popen(
            ['python3', 'app.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            # timeout=5,
        )

stdout = subp_script_res.stdout
stderr = subp_script_res.stderr

for line in subp_script_res.stdout:
    print(line)
    # sys.stdout.write(line)
    # logfile.write(line)



# for item in su

print("done")
