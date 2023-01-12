import socket


def get_content(host: str, port=80, buffer=4096) -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
        return s.recv(buffer)


def main():
    url = "scanme.nmap.org"
    print(get_content(url, port=80, buffer=400000))
    

if __name__ == "__main__":
    main()
