import csv
import sys
import socket
import time
import logging
import threading

def main():
    port = int(sys.argv[1],10)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
     s.bind(('local',port))
     s.listen(8)
    print("waiting for connections")
    w = csv.writer(csvfile=open('number.csv','w'))
    h = ['Event_timestamp', 'Node_name', 'Event', 'Log_timestamp', 'Message_length', 'Log_time']
    w.writerow(h)
    while True:
        conn,addr = s.accept()
        t = threading.Thread(target=TCP, args=(conn,))
        t.start()


def TCP(sock, w):
    while True:
        data = sock.recv(100)
        current_time = time.time()
        current_min  = time.localtime().tm_min
        current_sec  = time.localtime().tm_sec
        datas = data.decode()
        Log_line = format(datas)
        print(Log_line)
        x = Log_line.split()
        Event_timestamp = x[0]
        Node_name = x[1]
        Event = x[2]
        Message_length = len(Log_line)
        Log_timestamp = current_time
        Log_time = format(current_min,current_sec)
        data = [Event_timestamp, Node_name, Event, Log_timestamp, Message_length, Log_time]
        w.writerow(data)


    sock.close()



