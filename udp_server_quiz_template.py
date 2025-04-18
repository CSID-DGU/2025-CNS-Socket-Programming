import _____
from datetime import datetime

questions = [
    {"q": "문제1?", "a": "정답1?"},
    {"q": "문제2?", "a": "정답2?"},
    {"q": "문제3?", "a": "정답3?"}
]

UDP_PORT = _____
BUFFER_SIZE = _____

# 상태 변수
score = 0
current = 0
total = len(questions)
is_quiz_on = False

# UDP 소켓 생성 및 바인딩
sock = _____
_____
print(f"[UDP SERVER] Listening on port {UDP_PORT}")

while True:
    # 클라이언트 메시지 수신
    data, addr = _____
    msg = _____

    print(f"[RECV] ← 클라이언트 메시지 출력: {msg}")

    if msg == "/quiz":
        is_quiz_on = True
        score = 0
        current = 0
        response = f"문제 1: {questions[0]['q']}"

    elif msg.startswith("/answer") and is_quiz_on:
        user_answer = msg.split(" ", 1)[-1].strip()
        if user_answer == questions[current]['a'].lower():
            score += _____
            response = "정답입니다!"
        else:
            response = f"오답입니다. 정답은 {questions[current]['a']}입니다."

        current += _____
        if current < total:
            response += f"\n문제 {current + 1}: {questions[current]['q']}"
        else:
            is_quiz_on = False
            response += f"\n퀴즈 종료. 점수: {score}/{total}"

    elif msg == "/score":
        response = f"현재 점수는 {score}/{total}입니다."

    elif msg == "/exit":
        response = f"최종 점수: {score}/{total}. 수고하셨습니다!"
        # response 전송 함수 
        _____
        break

    else:
        response = "알 수 없는 명령어입니다."

    # 클라이언트에게 response 전송
    _____
    
print("[UDP SERVER] 종료됨")