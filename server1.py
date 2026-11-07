import socket

def interact_with_server2(msg,data):
    try:
        server2_soc.send(str(len(msg)).zfill(3).encode())
        server2_soc.send(msg.encode())
        server2_soc.send(str(len(data)).zfill(3).encode())
        server2_soc.send(data.encode())
        ans = server2_soc.recv(1024).decode()
    except Exception as e:
        ans = "1"

    return ans

#create the server
server_soc = socket.socket()
server_soc.bind(("0.0.0.0",53))
server_soc.listen(3)
#connect to main server


my_dict = {"1.1.1.1":"google", "2.2.2.2":"facebook"}
ans = "1"
while True:
    client_soc, addr = server_soc.accept()
    print(f"{addr[0]} - connected")
    while True:
        server2_soc = socket.socket()
        try:
            server2_soc.connect(("127.0.0.1", 54))
        except Exception as e:
            server2_soc.close()
        try:
            msg = client_soc.recv(1024).decode()
            data = client_soc.recv(1024).decode()
        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break

        if msg == "1":     #1 for ip
            print(data)
            if data in my_dict.keys():
                ans = my_dict[data]
            else:
                ans = interact_with_server2(msg,data)
                if not ans == "1":
                    my_dict[data] = ans

        else:       #if not 1 then its HOSTNAME
                for key in my_dict.keys():
                    if my_dict[key] == data:
                        ans = key
                        break
                if not ans == "1":
                    ans = interact_with_server2(msg,data)
                    if not ans == "1":
                        my_dict[ans] = data

        try:
            client_soc.send(ans.encode())
            break
        except Exception as e:
            print(f"error in receive or sending data {str(e)}")
            break
        client_soc.close()
        server2_soc.close()
    print(f"{addr[0]} - disconnected")
    client_soc.close()
    server2_soc.close()
