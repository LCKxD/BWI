import socket 
#Why are you looking at my code bro -_- ..... xD By: L  C  K

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

print("Welcome to the L  C  K Web basic info tool!")


print(" ")
server = raw_input('Enter a website: ')
port= 80
print(" ")
server_ip = socket.gethostbyname(server) 
print("Googles ip is "+server_ip)
print(" ")
request= "GET / HTTP/1.1\nHost: "+server+"\n\n" 

s.connect((server, port))
s.send(request.encode())
resutl= s.recv(4096)

print(resutl)

while (len(resutl) > 0):
	print(resutl)               
	result= s.recv(4096)