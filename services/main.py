import logging
import os
import socket
import subprocess
import time

HOLD = os.environ.get("HOLD_LOOP", "1")
MAX_HOST_RETRIES = 100

count = 0

logger = logging.getLogger(__name__)

while count < MAX_HOST_RETRIES:
    try:
        socket.gethostbyname("web")
        break
    except socket.error:
        logger.error("host is not up")
        time.sleep(0.1)
        count += 1
        continue

subprocess.run("nginx")


while HOLD == "1":
    time.sleep(0.1)
