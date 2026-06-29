import platform
import socket

def get_system_info():

    return f"""
Operating System : {platform.system()}
Release          : {platform.release()}
Version          : {platform.version()}

Machine          : {platform.machine()}
Processor        : {platform.processor()}

Hostname         : {socket.gethostname()}
Local IP         : {socket.gethostbyname(socket.gethostname())}
"""