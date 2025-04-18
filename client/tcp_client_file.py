import socket

SERVER_IP = "server2025"  # 컨테이너 내 hostname
TCP_PORT = 9151
BUFFER_SIZE = 1024

# 1. TCP 소켓 생성 및 연결
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, TCP_PORT))
print("[TCP CLIENT] 서버 연결 완료")

# 2. 명령 입력 및 전송
msg = input("[ME] 요청할 명령어 (/get 파일명 or /exit): ").strip()
sock.send(msg.encode())

# 3. 명령 처리
if msg.startswith("/get"):
    filename = msg.split(" ", 1)[-1]
    status = sock.recv(BUFFER_SIZE).decode()

    if status == "FOUND":
        with open(f"received_{filename}", "wb") as f:
            while True:
                data = sock.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
        print(f"[RECV] 파일 저장 완료: received_{filename}")
    else:
        print("[SERVER] 해당 파일 없음")

elif msg == "/exit":
    print(sock.recv(BUFFER_SIZE).decode())

# 4. 연결 종료
sock.close()
print("[TCP CLIENT] 연결 종료")
