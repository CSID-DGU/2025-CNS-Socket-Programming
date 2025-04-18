import _____ # 소켓 통신을 위한 기본 모듈
import os

SERVER_IP = _____  # 서버 컨테이너명
TCP_PORT = _____ # 사용할 포트 번호
BUFFER_SIZE = _____ # 한번에 송수신할 데이터 크기 (바이트 단위)

# TCP 소켓 생성 및 연결
sock = _____
# 서버 연결 시도
_____
print("[TCP CLIENT] 서버 연결 완료")

while True:
    cmd = input("[ME] 명령어 입력 (/list, /get <파일명>, /put <파일명>, /read <파일명>, /exit): ").strip()
    sock._____(cmd.encode()) # 명령어를 서버에 전송
    # 파일 목록 요청
    if cmd == "/list":
        file_list = sock._____(BUFFER_SIZE).decode()
        print("[SERVER FILE LIST]\n" + file_list)

    elif cmd.startswith("/get"):
        filename = cmd.split(" ", 1)[-1]
        status = sock._____(BUFFER_SIZE).decode()
        if status == "FOUND":
            with open(f"received_{filename}", "wb") as f:
                while True:
                    data = _____
                    if data.endswith(b"_END_"):
                        f.write(data[:-5])  # _END_ 제외하고 쓰기
                        break
                    f.write(data)
            print(f"[RECV] 저장 완료: received_{filename}")
        else:
            print("[SERVER] 해당 파일 없음")

    elif cmd.startswith("/put"):
        filename = cmd.split(" ", 1)[-1]
        if not os.path.exists(filename):
            print(f"[CLIENT] 파일 '{filename}' 없음")
            continue
        status = _____._____.decode()
        if status == "READY":
            with open(filename, "rb") as f:
                while True:
                    data = f._____(BUFFER_SIZE)
                    if not data:
                        break
                    sock.send(data)
            sock._____(b"_END_") # 전송 종료 신호
            print(f"[SEND] 업로드 완료: {filename}")

    elif cmd.startswith("/read"):
        filename = cmd.split(" ", 1)[-1]
        result = _____._____.decode()
        if result == "NOTFOUND":
            print("[SERVER] 해당 파일이 존재하지 않습니다.")
        else:
            print(f"[READ RESULT]\n{result}")

    elif cmd == "/exit":
        print(_____._____.decode()) # 서버 종료 메시지
        break

    else:
        print("[CLIENT] 지원되지 않는 명령어")

#TCP 연결 종료
sock._____
print("[TCP CLIENT] 연결 종료")
