import nmap

class NmapModule:
    def __init__(self):
        self.scanner = nmap.PortScanner()

    def scan(self, host, ports="1-1024"):
        self.scanner.scan(hosts=host, ports=ports, arguments='-sV')
        return self.scanner[host]