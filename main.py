import os
import subprocess
import time

from services.sync import sync_ingress
HOLD = os.environ.get("HOLD_LOOP", "1")

# write the conf file so nginx can start
sync_ingress()

# start nginx process
subprocess.run(["nginx", "-c", "/app/conf/nginx.conf"])

# keep nginx.conf synced with ingresses rules
while HOLD == "1":
    time.sleep(5)
    sync_ingress()
