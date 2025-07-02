# Do not run this code. This is sample code for a student who wanted to do server networking in python.
# Note: After running the program, open your web browser and go to http://localhost:9998

import socket
import threading

# Use 'localhost' for local access or '0.0.0.0' to allow access from other devices on your network.
IP = "0.0.0.0"
PORT = 9998


def main():
    """Main function to set up and run the server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    # Listen for up to 5 incoming connections in the queue
    server.listen(5)
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        # Accept a new connection from a client
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")

        # Create a new thread to handle the client connection
        client_handler = threading.Thread(target=handle_client, args=(client,))
        # Start the thread to run the handle_client function
        client_handler.start()
        #
        # FIXED: Removed client_handler.run()
        # Calling .run() would execute the handler in the main thread and block the server
        # from accepting new connections. .start() is all you need to begin the new thread.
        #


def handle_client(client_socket):
    """Handle an individual client connection."""
    # The 'with' statement ensures the socket is automatically closed
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received Request:\n{request.decode("utf-8")}')

        # FIXED: Send a proper HTTP response so the browser can display the page.
        # A browser expects a status line (HTTP/1.1 200 OK), headers, and a body.
        # The 'b' prefix converts the string to bytes for sending over the socket.
        http_response = b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<head><title>Success!</title></head>
<body>
<h1>ACK</h1>
<p>Hello! This is a response from your Python server.</p>
</body>
</html>
"""
        sock.sendall(http_response)


if __name__ == "__main__":
    main()