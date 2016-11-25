import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0)) #you can change this website! default is google but cnn is recommended because it changes all the time!
print "Your IP is: "+s.getsockname()[0]
