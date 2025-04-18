import socket
import os

TCP_PORT = 9151
BUFFER_SIZE = 1024

# 1. TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 포트 바인딩 및 대기
sock.bind(('', TCP_PORT))
sock.listen(1)
print(f"[TCP SERVER] Listening on port {TCP_PORT}")

# 3. 클라이언트 연결 수락
conn, addr = sock.accept()
print(f"[CONNECTED] {addr}")

# 4. 클라이언트 요청 수신
request = conn.recv(BUFFER_SIZE).decode().strip()
print(f"[REQUEST] {request}")

if request.startswith("/get"):
    filename = request.split(" ", 1)[-1]
    if os.path.exists(filename):
        conn.send("FOUND".encode())  # 클라이언트에게 OK 응답
        with open(filename, "rb") as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                conn.send(data)
        print(f"[SENT] File '{filename}' sent")
    else:
        conn.send("NOTFOUND".encode())  # 파일 없음 응답
elif request == "/exit":
    conn.send("BYE".encode())

# 연결 종료
conn.shutdown(socket.SHUT_WR)
conn.close()
print("[TCP SERVER] 연결 종료")
