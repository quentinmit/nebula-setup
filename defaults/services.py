import socket

__all__ = ["SERVICES"]

HOST = socket.gethostname()

#        type, host, title, settings path, autostart, loop_delay

SERVICES = {
    1  : ["broker", HOST, "broker",  None,                          False, 5],
    2  : ["meta",   HOST, "meta",    None,                          False, 5],
    3  : ["watch",  HOST, "watch",   "defaults/services/watch.xml", False, 5],
    4  : ["mesg",   HOST, "mesg",    "defaults/services/mesg.xml",  True,  5],
    5  : ["conv",   HOST, "conv01",  None,                          False, 5],
}
