"""最簡單的 Socket 伺服器端

執行方式：python server.py
等待客戶端連線，接收訊息並回傳「Echo: 原始訊息」。
"""

import socket

HOST = "127.0.0.1"  # 只接受本機連線
PORT = 65432        # 埠號（1024~65535 皆可）


def main():
    # AF_INET: 使用 IPv4；SOCK_STREAM: 使用 TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()  # 開始監聽連線

        print(f"伺服器啟動，監聽 {HOST}:{PORT} ...")

        # 接受一個客戶端連線
        conn, addr = server_socket.accept()
        with conn:
            print(f"客戶端已連線：{addr[0]}:{addr[1]}")
            while True:
                data = conn.recv(1024)  # 最多接收 1024 bytes
                if not data:
                    break  # 客戶端關閉連線

                message = data.decode("utf-8")
                print(f"收到：{message}")

                if message.lower() == "quit":
                    conn.sendall("伺服器已關閉連線".encode("utf-8"))
                    break

                response = f"Echo: {message}"
                conn.sendall(response.encode("utf-8"))  # 回傳訊息

        print("連線結束")


if __name__ == "__main__":
    main()
