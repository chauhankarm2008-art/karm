import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        hostname = socket.getfqdn(domain)

        return f"""Hostname : {hostname}

IP Address : {ip}
"""
    except:
        return "Invalid Domain"