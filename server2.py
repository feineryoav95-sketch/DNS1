import socket


#create the server
server2_soc = socket.socket()
server2_soc.bind(("0.0.0.0",54))
server2_soc.listen(3)


my_dict = {"1.1.1.1":"google", "2.2.2.2":"facebook", "3.3.3.3":"instagram", "4.4.4.4":"whatsapp"}
while True:
    server1_soc, addr = server2_soc.accept()
    print(f"{addr[0]} - connected")
    while True:
        try:
            msg_len = int(server1_soc.recv(3).decode())
            msg = server1_soc.recv(msg_len).decode()
            data_len = int(server1_soc.recv(3).decode())
            data = server1_soc.recv(data_len).decode()
        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break
        ans = "1"
        if msg == "1":      #client entered IP
            if data in my_dict.keys():
                ans = my_dict[data]
        else:               #if it is not 1 then its HOSTNAME
            print(data)
            if data in my_dict.values():
                for key in my_dict.keys():
                    if my_dict[key] == data:
                        ans = key
        try:
            server1_soc.send(ans.encode())
        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break
        server1_soc.close()
    print(f"{addr[0]} - disconnected")
    server1_soc.close()