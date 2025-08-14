import socket
import threading
import os

BUFFER_SIZE = 4096
PORT = 4583
DISCOVERY_TIMEOUT = 10  # seconds

def discover_server_ip(timeout=DISCOVERY_TIMEOUT):
    """Listens for a broadcast from the server to discover its IP."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    listener.bind(("", PORT))
    listener.settimeout(timeout)

    print("[*] Listening for server broadcast...")
    try:
        data, addr = listener.recvfrom(1024)
        server_ip = data.decode()
        print(f"[+] Server discovered at: {server_ip}")
        return server_ip
    except socket.timeout:
        print("[!] Server broadcast not received.")
        return None
    finally:
        listener.close()

def receive_full_data(sock):
    """Receives data from server until <EOF> is found."""
    data = b""
    while True:
        chunk = sock.recv(BUFFER_SIZE)
        if not chunk:
            break
        if chunk.endswith(b"<EOF>"):
            data += chunk[:-5]
            break
        data += chunk
    return data

def connect_to_server(ip):
    """Connects to the server and starts terminal-style input."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, PORT))
    print(f"[+] Connected to server at {ip}:{PORT}\n")

    try:
        while True:
            cmd = input(">> $ ").strip()

            if not cmd:
                continue

            if cmd.upper().startswith("UPLOAD "):
                _, filename = cmd.split(maxsplit=1)
                if os.path.exists(filename):
                    client.send(f"UPLOAD {filename}".encode())
                    with open(filename, "rb") as f:
                        while chunk := f.read(BUFFER_SIZE):
                            client.send(chunk)
                        client.send(b"<EOF>")
                    response = client.recv(BUFFER_SIZE).decode()
                    print(response)
                else:
                    print("[!] File not found.")

            elif cmd.upper().startswith("DOWNLOAD "):
                _, filename = cmd.split(maxsplit=1)
                client.send(f"DOWNLOAD {filename}".encode())
                data = receive_full_data(client)
                if data == b"File not found.":
                    print("[!] File not found on server.")
                else:
                    with open(filename, "wb") as f:
                        f.write(data)
                    print("[*] File downloaded.")

            elif cmd.upper() == "EXIT":
                client.send(b"EXIT")
                print(client.recv(BUFFER_SIZE).decode())
                break

            else:
                # Treat everything else as a shell command
                client.send(f"COMMAND {cmd}".encode())
                output = client.recv(BUFFER_SIZE).decode()
                print(output)

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        client.close()
        print("[*] Disconnected from server.")

if __name__ == "__main__":
    server_ip = discover_server_ip()
    if server_ip:
        connect_to_server(server_ip)
