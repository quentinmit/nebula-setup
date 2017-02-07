import socket

__all__ = ["SERVICES"]

HOST = socket.gethostname()

#        type, host, title, settings path, autostart, loop_delay
SERVICES = {
    1 : ["mesg",   HOST, "mesg",   None, True, 5],
    2 : ["broker", HOST, "broker", None, True, 5],
    3 : ["meta",   HOST, "meta",   None, True, 5]
}
