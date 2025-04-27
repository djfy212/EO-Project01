# 무명의 기억 저장하는 코드
# modules/memory_storage.py

import json
import os
# 파일의 경로
MEMORY_FILE = "data/memory.json"

def store_sensation(sensation_data): # 감응데이터(하나)가 매개변수
    """
    감응 데이터를 무명의 기억 저장소(memory.json)에 저장하는 함수
    """
    # 1. memory.json 파일이 있는지 확인하고, 없으면 새로 만든다
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)
    
    # 2. 기존 저장된 데이터를 불러온다
    with open(MEMORY_FILE, "r") as f:
        memory_list = json.load(f)          # 📖 일기장을 손에 든다
    
    # 3. 새 감응 데이터를 리스트에 추가한다
    memory_list.append(sensation_data)      # ✏️ 메모지에 새 내용 추가

    # 4. 다시 파일에 저장한다
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_list, f, indent=4) # 📖 새로 쓴 일기장 다시 꽂는다