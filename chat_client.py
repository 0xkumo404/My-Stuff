import socket
import threading

def receive_messages(client_socket):
    """Receive and print messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode())
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

def main():
    """Connect to the server and handle user input."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))  # Connect to server (localhost, port 12345)
    print("Established connection")

    # Start a thread to receive messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Send messages to the server
    while True:
        try:
            message = input()
            client_socket.send(message.encode())
        except:
            print("Disconnected from the server.")
            client_socket.close()
            break

if __name__ == "__main__":
    main()
