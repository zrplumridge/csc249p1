#!/usr/bin/env python3
# Simple server test client
#
# This simple client application can be used to test a server that is under development.
# The application opens a connection to the server, then goes into a loop where it prompts
# the user to provide a string message to be sent over to the server for processing. Then
# the client waits for a reply and prints it. To exit and disconnect, the user can enter 'quit'
# at the prompt.

import socket

HOST = "127.0.0.1"  # This is the loopback address
PORT = 65432        # The port used by the server

def run_client():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(s):
                break

def talk_to_server(sock):
    msg = input("What message would you like to send to the server? ")
    if msg == 'quit':
        print("client quitting at operator request")
        return False
    print(f"sending message '{msg}' to server")
    sock.sendall(msg.encode('utf-8'))
    print("message sent, waiting for reply")
    reply = sock.recv(1024)
    if not reply:
        return False
    else:
        print(f"received reply '{reply}' from server")
        return reply

if __name__ == "__main__":
    run_client()
    print("test client is done, exiting...")
