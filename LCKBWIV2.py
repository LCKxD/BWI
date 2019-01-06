#!/usr/bin/python
import socket
#Why are you looking at my code bro -_- ..... xD By: L  C  K



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Welcome to the L C  K basic web info tool!")
print("")
print("This is a simple tool to help ather infomation on  web server. Includes Ip infomation and the specified HTTP verb info")



print(" ")
server = input('Enter a website: ')
hverb= input('Enter the HTTP Verb to use(Should be all uppercase): ')
port= 80
print(" ")
server_ip = socket.gethostbyname(server)
print( server + " ip is "+server_ip)
print(" ")
request= hverb +" / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server, port))
s.send(request.encode())
resutl= s.recv(2048)

print(resutl)
