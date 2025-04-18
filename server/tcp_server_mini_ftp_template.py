import _____ # 소켓 통신을 위한 기본 모듈
import os

TCP_PORT = _____ # 사용할 포트 번호
BUFFER_SIZE = _____ # 한번에 송수신할 데이터 크기 (바이트 단위)

#TCP 소켓 생성
sock = _____
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #OSError: [Errno 98] Address already in use 오류 방지를 위한 코드
#소켓 바인딩 (모든 인터페이스에서 접속 허용)
_____
# 클라이언트 최대 1명까지 대기
_____
print(f"[TCP SERVER] Listening on port {TCP_PORT}")

# 클라이언트 연결 수락
_____ # 연결 수락 후 소켓 객체(conn)와 주소(addr) 반환
print(f"[CONNECTED] {addr}")

while True:
    try:
        request = _____._____.decode().strip() # 클라이언트 요청 수신 및 디코딩
        if not request:
            break
        print(f"[REQUEST] {request}")

        if request == "/list":
            files = os.listdir(".")
            file_list = "\n".join(files)
            conn._____(file_list.encode()) # 결과 전송

        elif request.startswith("/get"):
            filename = request.split(" ", 1)[-1].strip()
            if os.path.exists(filename):
                conn.send("FOUND".encode())
                with open(filename, "rb") as f:
                    while True:
                        data = f.read(BUFFER_SIZE)
                        if not data:
                            break
                        conn.send(data)
                conn.send(b"_END_")  # 전송 종료 신호
                print(f"[SENT] {filename}")
            else:
                conn.send("NOTFOUND".encode())

        elif request.startswith("/put"):
            filename = request.split(" ", 1)[-1].strip()
            conn.send("READY".encode())
            with open(f"put_{filename}", "wb") as f:
                while True:
                    data = conn._____
                    if data.endswith(b"_END_"):
                        f.write(data[:-5])
                        break
                    f.write(data)
            print(f"[RECV] 업로드 완료: put_{filename}")

        elif request.startswith("/read"):
            filename = request.split(" ", 1)[-1].strip()
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                conn.send(content.encode())
                print(f"[READ] 파일 내용 전송 완료: {filename}")
            else:
                conn.send("NOTFOUND".encode())

        elif request == "/exit":
            conn.send("BYE".encode())
            break

        else:
            conn.send("INVALID".encode())

    except Exception as e:
        print(f"[ERROR] {e}")
        break
    
#TCP 연결 종료
conn._____
print("[TCP SERVER] 연결 종료")
