"""最簡單的 Socket 客戶端

執行方式：python client.py
連線到伺服器後，從終端機輸入訊息傳送，顯示伺服器回應。
輸入 quit 離開。
"""

import socket

HOST = "127.0.0.1"  # 伺服器位址
PORT = 65432        # 伺服器埠號（需與 server.py 一致）


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # 連線到伺服器
        print(f"已連線到 {HOST}:{PORT}，輸入訊息（quit 離開）：")

        while True:
            message = input("> ").strip()
            if not message:
                continue

            client_socket.sendall(message.encode("utf-8"))  # 傳送訊息

            if message.lower() == "quit":
                print(client_socket.recv(1024).decode("utf-8"))
                break

            response = client_socket.recv(1024).decode("utf-8")  # 接收回應
            print(f"伺服器回應：{response}")

    print("已斷線")


if __name__ == "__main__":
    main()
