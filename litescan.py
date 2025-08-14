import socket  # Importing connection module

# Target IP and port range
#          IP adress is here
#           vvvvvvvvvvvvvv
target_ip = "10.253.19.79"
start_port = 1
end_port = 500

# Initialize variables
port_finds = []
total_ports = end_port - start_port + 1  # Total number of ports to check

# Start scanning
print("Checking for open ports...")
print('')
for index, port in enumerate(range(start_port, end_port + 1), start=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)  # Set timeout for connection attempts
        result = s.connect_ex((target_ip, port))  # Attempt to connect

        if result == 0:
            print(f"Port {port} is open")
            port_finds.append(port)
        else:
            print(f"Port {port} is closed")

        # Calculate and display progress
        progress = (index / total_ports) * 100
        rounded = round(progress, 3)
        print(f"                        {rounded}%")

# Final results
print("\nScan Complete!")
print('')
if port_finds:
    print('Open ports found!')
    print(f"Open ports: {port_finds}")
else:
    print("No open ports found :(")
