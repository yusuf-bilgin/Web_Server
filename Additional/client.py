import socket
import sys

# Get the server address, port and filename from command line arguments
server_address = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_address, server_port))

# Send an HTTP GET request for the requested file
request = f"GET /{filename} HTTP/1.1\r\nHost: {server_address}\r\n\r\n"
client_socket.send(request.encode())

# Receive the server's response
response = ""
while True:
    data = client_socket.recv(4096).decode()
    if not data:
        break
    response += data

# Print the response
print(response)

# Close the socket
client_socket.close()
