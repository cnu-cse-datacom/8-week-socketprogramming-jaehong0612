import socket

socket_recv = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_recv.bind(('',9000))
print("file recv start from 127.0.0.1")

data, addr = socket_recv.recvfrom(1024)
print(data)
file_name = data.decode()
print("File Name :"+file_name)

data, _ = socket_recv.recvfrom(1024)
file_size = data.decode()
print("File Size :"+file_size)

recive_file = open(file_name,'wb')
recive_size = 0

while True:
	data,addr = socket_recv.recvfrom(1024)
	if not data:
		break
	recive_file.write(data)
	recive_size += len(data)
	print("current_size / total_size = "+ "%d / %d, %.6f %%" %(recive_size,int(file_size),(recive_size/int(file_size))*100))
	if (int(file_size) == recive_size):
		break


recive_file.close()
	
		



