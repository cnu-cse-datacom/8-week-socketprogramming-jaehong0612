import socket
import os
ip_addr = '192.168.0.6'
port = 9000

file_name = input("Input your file name :")
print("File Transmit Start......")

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

send_file = open(file_name,'rb')
file_size = os.path.getsize(file_name)

socket.sendto(file_name.encode(),(ip_addr,port))
socket.sendto(str(file_size).encode(),(ip_addr,port))

file_sendlength = 0;
while True:
    data = send_file.read(1024)
    if not data : 
        print("ok")
        print("file_send_end")
        break
    
    socket.sendto( data , (ip_addr,port))
    file_sendlength += len(data)
    print("current_size / total_size = "+ "%d / %d %.6f %%" %(file_sendlength,file_size,(file_sendlength/file_size)*100) )

send_file.close()



