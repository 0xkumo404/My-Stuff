import socket
import threading

# List to keep track of connected clients
clients = []

def handle_client(client_socket):
    """Handles communication with a single client."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                # Broadcast the message to all clients
                broadcast(message, client_socket)
            else:
                # Remove client if disconnected
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    """Sends a message to all clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)
                client.close()

def main():
    """Sets up the server and listens for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))  # Bind to all network interfaces, port 12345
    server_socket.listen(5)  # Allow 5 queued connections
    print("Server is listening on port 12345...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)

        # Create a thread for handling the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()
