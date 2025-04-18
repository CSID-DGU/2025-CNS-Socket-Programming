import socket
from datetime import datetime

UDP_PORT = 9152
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))

print(f"[UDP SERVER] Listening on port {UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode().strip().lower()
    print(f"[CLIENT] {addr} → {msg}")

    if msg == "/time":
        reply = f"현재 시각은 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}입니다."
    elif msg == "/hello":
        reply = "안녕하세요, UDP 서버입니다!"
    elif msg == "/exit":
        reply = "연결 종료합니다."
        sock.sendto(reply.encode(), addr)
        break
    else:
        reply = "알 수 없는 명령입니다."

    sock.sendto(reply.encode(), addr)

print("[UDP SERVER] 종료됨.")