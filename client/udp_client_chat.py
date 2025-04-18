import socket

SERVER_IP = "server2025"
UDP_PORT = 9152
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[UDP CLIENT] 명령어 입력 시스템 시작")
print("가능한 명령어: /time, /hello, /exit")

while True:
    msg = input("[ME] → ")
    sock.sendto(msg.encode(), (SERVER_IP, UDP_PORT))

    data, _ = sock.recvfrom(1024)
    reply = data.decode()
    print(f"[SERVER] → {reply}")

    if msg.strip().lower() == "/exit":
        break

print("[UDP CLIENT] 종료됨.")