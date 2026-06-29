import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_ports(target):
    results = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return [("ERROR", "Invalid Hostname")]

    # Scan only common ports (fast)
    for port in COMMON_PORTS.keys():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            results.append((port, COMMON_PORTS[port]))

        sock.close()

    return results