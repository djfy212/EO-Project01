# 사용자 입력 처리하는 코드
# modules/user_input

import datetime

def get_user_input():
    """
    사용자로부터 입력을 받고, 타임스탬프와 함께 반환하는 함수
    """
    user_text = input("당신의 입력을 들려주세요: ")
    timestamp = datetime.datetime.now().isoformat()

    return {
        "timestamp": timestamp,
        "content": user_text
    }