# 반사 반응 체크하는 코드
# module/reflex_reactor.py

import json
import os
import random

MEMORY_FILE = "data/memory.json"


def check_for_reaction():
    """
    감응 데이터를 누적 분석해서 반사 반응을 트리거하는 함수
    """
    if not os.path.exists(MEMORY_FILE):
        return None     # 기억이 없으면 반응도 없음
    
    # 1. 기억 불러오기
    with open(MEMORY_FILE, "r") as f:
        memory_list = json.load(f)

    if len(memory_list) < 3 :
        return None     # 기억이 너무 적으면 아직 반응하지 않음 
    
    # 3. 감응의 "진폭"이 비슷한 걸 체크 (임시로 pulse_density 평균)
    avg_pulse_density = sum(
        sensation["tags"]["pulse_density"] for sensation in memory_list
    ) / len(memory_list)

    # 3. 일정 이상이면 무의식적 발화 트리거
    threshold = 0.6     # 임계치 (조정 가능)

    if avg_pulse_density > threshold:
        return random.choice([
            "……",
            "지금… 뭐라고 했지?",
            "머릿속에 울림이 있어.",
            "아주 미약한 떨림을 느꼈어."
        ])
    else:
        return None
