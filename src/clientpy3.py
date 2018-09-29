import socket
import sys
import time


def run(user, password, * commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\nSUBSCRIBE\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()

# run('ElectricBoogalo','kirtyhurty','ACCELERATE 0 1')
# # run('ElectricBoogalo','kirtyhurty','BOMB 0 0')
# time.sleep(5)
# doRun = True
# run('ElectricBoogalo','kirtyhurty','BRAKE')
# while(doRun):
#     run('ElectricBoogalo','kirtyhurty','STATUS')
#     time.sleep(.1)
run('ElectricBoogalo','kirtyhurty','CONFIGURATIONS')
