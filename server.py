import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is waiting for client connection...")

conn, addr = server_socket.accept()
print("Connected to client:", addr)

while True:
    data = conn.recv(1024).decode()
    if data.lower() == "exit":
        print("Client disconnected")
        break
    print("Client:", data)
    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
server_socket.close()

