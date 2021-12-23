import socket

class Ports:
    def __init__(self):
        self.begin = 1
        self.end = 64738
        self.timeout = 0.2
        self.openned = []

class Pyscan:
    def __init__(self):
        self.ports = Ports()
        self.host = input("host: ")

        self.scan()
        self.resume()

    def scan(self):
        print("time estimated: {}s / port | total ports: {} | total time: {:.0f}s".format(
            self.ports.timeout,
            self.ports.begin + self.ports.end,
            self.ports.timeout * (self.ports.begin + self.ports.end)
        ))
        print("scanning...")
        for port in range(self.ports.begin, self.ports.end):
            if (self.check(port) == True):
                self.ports.openned.append("{}:{}".format(self.host, port))
        print("scan ended")
    
    def check(self, port):
        s = socket.socket()
        s.settimeout(self.ports.timeout)
        try:
            s.connect((self.host, port))
            return (True)
        except:
            return (False)

    def resume(self):
        for openned in self.ports.openned:
            print("[+] {}".format(openned))

if (__name__ == "__main__"):
    Pyscan()
