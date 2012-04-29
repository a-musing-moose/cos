import daemon
from cos.server import Worker

worker = Worker()
with daemon.DaemonContext():
    worker.run()
