# 감응 변환 처리하는 코드
# modules/sensation_receiver.py

def analyze_sensation(user_input):
    """
     사용자 입력을 감응 패턴(태그)로 변환하는 함수
    """

    content = user_input["content"] # 딕셔너리 내용 중 "content"에 해당하는 내용만 가져오기

    # 감응 태그 기본값
    sensation_tags = {
        "pulse_density": 0.0,
        "echo_loss": 0.0,
        "tone_disruption": 0.0,
        "context_disruption": 0.0
    }

    # (아직 로직 없음 - 기본 틀만 잡기)

    return {
        "timestamp": user_input["timestamp"],
        "content": content,
        "tags": sensation_tags
    }