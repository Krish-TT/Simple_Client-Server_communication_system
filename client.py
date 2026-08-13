import socket
import time

SERVER_IP = '10.21.16.52'
PORT = 9999
CLIENT_NAME = "Client/Krish_Seksaria"

def run_client():
    try:
        client_val = int(input("Enter an integer between 1 and 100: "))
    except ValueError:
        print("[!] Invalid input. Please enter a valid integer.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, PORT))

        payload = f"{CLIENT_NAME}|{client_val}"
        client_socket.sendall(payload.encode('utf-8'))

        reply = client_socket.recv(1024).decode('utf-8')

        if reply:
            server_name, server_val_str = reply.split('|')
            server_val = int(server_val_str)
            total_sum = client_val + server_val

            print(f"Client Name   : {CLIENT_NAME}")
            print(f"Server Name   : {server_name}")
            print(f"Client Integer: {client_val}")
            print(f"Server Integer: {server_val}")
            print(f"Sum           : {total_sum}")

    except ConnectionRefusedError:
        print("[!] Error: Server is not running or port is blocked.")
    except Exception as e:
        print(f"[!] Network error: {e}")
    finally:
        client_socket.close()
        print("[*] Socket released. Client terminated.")


if __name__ == "__main__":
        run_client()
