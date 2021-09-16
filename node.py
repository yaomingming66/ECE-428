import sys
import socket
import time

def main():
    Node_name = sys.argv[1]
    IP = sys.argv[2]
    port = int(sys.argv[3],10)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP,port))
        s.send(format(time.time(), Node_name).encode())
        while True:
            data = input()
            print(data)
            split = data.split()
            timestamp = split[0]
            Event = split[1]
            s.send(format(timestamp, Node_name, Event).encode())


if __name__ == '__main__':
   pass