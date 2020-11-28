import os
import subprocess
import time

HOLD = os.environ.get("HOLD_LOOP", "1")

subprocess.run("nginx")


while HOLD == "1":
    time.sleep(0.1)
