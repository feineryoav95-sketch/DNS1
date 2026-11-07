import socket
def getIP():
    """
    param:none
    :return:IP address
    """
    while True:
        ans = True
        IP = input("enter an IP: ")
        list_IP = IP.split(".")
        if len(list_IP) == 4:
            for i in list_IP:
                if not i.isdigit() or int(i) > 255:
                    ans = False
            if ans:
                break
    return IP

def interact_with_server(msg,ans):
    try:
        my_sock.send(msg.encode())
        my_sock.send(ans.encode())
        ret_ans = my_sock.recv(1024).decode()
    except Exception as e:
        ret_ans = "1"
    return ret_ans


my_sock = socket.socket()

my_dict = {"1.1.1.1":"google"}

#connect to server

#open1 = False
while True:
    my_sock = socket.socket()
    try:
        my_sock.connect(("127.0.0.1", 53))
    except Exception as e:
        my_sock.close()
        exit(f"server is down - try again {str(e)}")

    msg = input("enter 1 for IP, 2 for HostName, 3 for Exit: ")
    if msg == "1":
        ans = getIP()
        if ans in my_dict.keys():
            print(my_dict[ans])
        else:
            ans1 = interact_with_server(msg,ans)
            if not ans1 == "1":
                my_dict[ans] = ans1
                print(ans1)
            else:
                print("No HOSTNAME found for IP entered")
    elif msg == "2":
        ans = input("enter HostName: ")
        if ans in my_dict.values():
            for key in my_dict.keys():
                if my_dict[key] == ans:
                    print(key)
                    break
        else:
            ans1 = interact_with_server(msg,ans)
            if not ans1 == "1":
                my_dict[ans1] = ans
                print(ans1)
            else:
                print("No IP found for HOSTNAME entered")
    elif msg == "3":
        break

    else:
        print("invalid input: try again!")
        continue

    my_sock.close()


my_sock.close()
print("Bye Bye, have a great day!")