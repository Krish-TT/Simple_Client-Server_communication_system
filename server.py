import random
import socket
import sys

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 9999
SERVER_NAME = "Server/Krish_Seksaria"
server_int = random.randint(1, 100)
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"[{SERVER_NAME}] Server running and listening on port {PORT}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"\n[+] Incoming connection established from {client_address}")

            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    client_socket.close()
                    continue

                # Client Name|Client Integer
                client_name, client_val_str = data.split('|')
                client_val = int(client_val_str)
                if not (1 <= client_val <= 100):
                    print(f"[!] Received out-of-bounds integer ({client_val}). Terminating connection...")
                    client_socket.close()
                    server_socket.close()
                    sys.exit(0)

                total_sum = client_val + server_int
                print("--- Server Output Log ---")
                print(f"Client Name   : {client_name}")
                print(f"Server Name   : {SERVER_NAME}")
                print(f"Client Value  : {client_val}")
                print(f"Server Value  : {server_int}")
                print(f"Calculated Sum: {total_sum}")

                # Send back: Server Name|Server Integer
                response = f"{SERVER_NAME}|{server_int}"
                client_socket.sendall(response.encode('utf-8'))

            except Exception as e:
                print(f"[!] Processing error: {e}")
            finally:
                client_socket.close()

    except KeyboardInterrupt:
        print("\n[*] Server manual shutdown requested.")
    finally:
        server_socket.close()
        print("[*] All server sockets closed safely.")

if __name__ == "__main__":
    run_server()
