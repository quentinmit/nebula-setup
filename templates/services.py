import socket

__all__ = ["SERVICES"]

HOST = socket.gethostname()

#        type, host, title, settings path, autostart, loop_delay

SERVICES = {
    1  : ["broker", HOST, "broker",  None,                 True, 5],
    2  : ["meta",   HOST, "meta",    None,                 True, 5],
    3  : ["watch",  HOST, "watch",   "services/watch.xml", True, 5],
    4  : ["mesg",   HOST, "mesg",    "services/mesg.xml",  True, 5],
    5  : ["conv",   HOST, "conv01",  None,                 True, 5],
    6  : ["conv",   HOST, "conv02",  None,                 True, 5],
    7  : ["conv",   HOST, "conv03",  None,                 True, 5],
    8  : ["conv",   HOST, "conv04",  None,                 True, 5],
    9  : ["conv",   HOST, "conv05",  None,                 True, 5],
    10 : ["conv",   HOST, "conv06",  None,                 True, 5],
    11 : ["conv",   HOST, "conv07",  None,                 True, 5],
    12 : ["conv",   HOST, "conv08",  None,                 True, 5],
    13 : ["conv",   HOST, "conv09",  None,                 True, 5],
    14 : ["conv",   HOST, "conv10",  None,                 True, 5],
    15 : ["conv",   HOST, "conv11",  None,                 True, 5],
    16 : ["conv",   HOST, "conv12",  None,                 True, 5],
    17 : ["conv",   HOST, "conv13",  None,                 True, 5],
    18 : ["conv",   HOST, "conv14",  None,                 True, 5],
    19 : ["conv",   HOST, "conv15",  None,                 True, 5],
    20 : ["conv",   HOST, "conv16",  None,                 True, 5],
}
