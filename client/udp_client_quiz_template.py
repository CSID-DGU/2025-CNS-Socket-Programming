import _____

SERVER_IP = _____
UDP_PORT = _____
BUFFER_SIZE = _____

# UDP 소켓 생성
sock = _____

print("[UDP CLIENT] 퀴즈 챗봇 시작")
print("사용 가능한 명령어: /quiz, /answer <내용>, /score, /exit")

while True:
    msg = input("[ME] → ").strip()

    # 서버에 메시지 전송
    _____

    # 서버 응답 수신
    data, _ = _____
    reply = _____

    print(f"[SERVER] → {reply}")

    if msg.lower() == "/exit":
        break

print("[UDP CLIENT] 종료됨")