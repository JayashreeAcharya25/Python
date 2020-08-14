import socket
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)
print("Computer Name:" + hostname)
print("Computer IP Address:" + ipaddress)