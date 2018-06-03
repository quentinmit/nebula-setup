import socket

__all__ = ["SERVICES"]

HOST = socket.gethostname()

#        type, host, title, settings path, autostart, loop_delay

SERVICES = {
    1  : ["broker", HOST, "broker",  None,                          True, 5],
    2  : ["mesg",   HOST, "mesg",    "defaults/services/mesg.xml",  True, 5],
    3  : ["meta",   HOST, "meta",    None,                          True, 5],
    4  : ["conv",   HOST, "conv01",  None,                          True, 5],
}
