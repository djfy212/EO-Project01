# 감응/반응 기록 저장하는 코드
# modules/sensation_logger.py

import json
import os

LOG_FILE = "data/log.json"

def log_sensation(sensation_data, reaction=None):
    """
    감응 데이터와 반응 결과를 로그 파일에 저장하는 함수
    """

    # 1. log.json 파일이 있는지 확인하고, 없으면 새로 만든다
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)
    
    # 2. 기존 로그 불러오기
    with open(LOG_FILE, "r") as f:
        log_list = json.load(f)  #log파일을 변수에 딕셔너리 형식으로 저장(메모리)
    
    # 3. 새로운 로그 항목 만들기
    log_entry = {
        "timestamp": sensation_data["timestamp"],
        "content": sensation_data["content"],
        "tags": sensation_data["tags"],
        "reaction": reaction    # 반응이 없으면 None 저장
    }

    # 4. 로그에 추가
    log_list.append(log_entry)

    # 5. 다시 저장
    with open(LOG_FILE, "w") as f:
        json.dump(log_list, f, indent=4)