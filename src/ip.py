import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockfd.connect(('255.255.255.0', 0))  
print("Your LAN IP address is %s" % sockfd.getsockname()[0])
sockfd.close()
