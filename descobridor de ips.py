import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == "__main__":
    ip = get_ip_address()
    print(f"O endereço IP do computador é: {ip}")