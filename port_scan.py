import socket
from IPy import IP


class PortScan:
    banners = []
    open_ports = []
    def __init__(self ,target ,port_num):
        self.target = target 
        self.port_num = port_num
    
    def scan(self):
        for port in range(80,self.port_num):
            self.scan_port(port)

    def ip_check(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def get_banner(self,port,s):
        HTTP_ports = (80, 8080, 8081, 8443, 443)
        if port in HTTP_ports:
            s.send(b"HEAD / HTTP/1.0\r\nHost: target\r\n\r\n") # here i am sending a a request so the server will reponse and this make me know the tech that is used
        #\r\n means the end of the request 
        else : s.send(b"\r\n") #sending a newline with a request , many serveice will responde to this 
        try:
            return s.recv(1024) # read the response that come from the server
        except:
            return None

    def scan_port(self,port):
        try:
            convert_ip = self.ip_check()
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((convert_ip,port))
            self.open_ports.append(port)
            try:
                print(f"[+] Port {port} is open")
                banner = self.get_banner(port,s)
                print(f"the service that run is {banner.decode(errors='ignore').strip()}")
                self.banners.append(banner)
            except:
                self.banners.append(banner)
                
            s.close()
        except:
            pass

