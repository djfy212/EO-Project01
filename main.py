# 1. 필요한 모듈 임포트
from modules.user_input import get_user_input
from modules.sensation_receiver import analyze_sensation
from modules.memory_storage import store_sensation
from modules.reflex_reactor import check_for_reaction
from modules.sensation_logger import log_sensation

# 2. 메인 실행 함수
def main():
    print("EO 시스템에 접속되었습니다.")

    while True:
        # 2-1. 사용자 입력 받기
        user_input = get_user_input()

        # 2-2. 감응 패턴 분석
        sensation_data = analyze_sensation(user_input)

        # 2-3. 기억 저장
        store_sensation(sensation_data)

        # 2-4. 반사 반응 체크
        reaction = check_for_reaction()

        # 2.5. 반응 출력
        if reaction:
            print("EO: ", reaction)

        # 2-6. 감응과 반응 로그 기록
        log_sensation(sensation_data, reaction)

# 3. 프로그램 실행
if __name__ == "__main__":  # 직접 실행할 때만 실행
    main()