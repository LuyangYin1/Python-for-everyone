# Do not run this code. This is sample code for a student who wanted to do server networking in python. 
#   Note : run the program, open chrome and go to webpage https://localhost:9998

import socket
import threading
IP = '0.0.0.0'
PORT = 9998
def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((IP, PORT))
  server.listen(5)
  print(f'[*] Listening on {IP}:{PORT}')
 
  while True:
    client, address = server.accept()
    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    client_handler.run()

def handle_client(client_socket):
   with client_socket as sock:
     request = sock.recv(1024)
     print(f'[*] Received: {request.decode("utf-8")}')
     sock.send(b'ACK')

if __name__ == '__main__':
   main()
   # after running the program open chrome and go to webpage https://localhost:9998

