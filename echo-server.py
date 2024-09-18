#!/usr/bin/env python3
#by Zoe Plumridge
#instructions discussed with Emi Neuwalder, ideas discussed with Vivian Streber
#Due Friday Sept 20 2024

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data: #if no data present here / empty
                break
            #confirms receipt of message
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            #calculates number of times to repeat output based on first character
            length = int.from_bytes(data[:1], byteorder="little") - 48
            #if first character is not a number, will default to 5 repeats
            if length > 20:
                length = 5
            print(f"Times to be repeated is '{length!r}'")

            #converts lowercase values to uppercase
            data = data[1:].upper() #+ bytes('', 'utf-8')

            #loops through to send output multiple times
            for x in range(length):
                print(f"echoing '{data!r}' back to client")
                conn.send(data)
                
            #conn.sendall(data)
            conn.close()

            # words = data.split()
            # #length = words[:32]
            # length = int.from_bytes(words[0], "big")
            # #words.pop() #this converts it to a list which is not helpful
            # for x in range(length):
            #     #print(f"echoing '{words!r}' back to client")
            #     #words[1] = words[1].upper()
            #     print(f"echoing '{words!r}' back to client")
            #     #conn.sendall(words)
            # #words = words.upper()
            # #print(f"echoing '{words!r}' back to client")
            # conn.sendall(bytes(words, 'utf-8'))

print("server is done!")
