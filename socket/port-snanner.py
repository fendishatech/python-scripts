import socket
import threading

target_host = "example.com"
open_ports = []


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_host, port))
    if result == 0:
        open_ports.append(port)
    sock.close()


def main():
    threads = []

    for port in range(1,1025):
        thread = threading.Thread(target=scan_port,args=(port,))

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Open ports:", open_ports)

if __name__ == "__main__":
    main()