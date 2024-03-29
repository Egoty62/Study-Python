# 정규 표현식 (regex)
# 정규 표현식은 일종의 문자를 표현하는 공식
    # 특정 규칙이 있는 문자열 집합을 추출할 때 자주 사용하는 기법
        # ex) 010-0000-0000 => ^\d{3}-\d{4}-\d{4}$
        # ex) 203.252.101.40 => ^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$
            # 시작은 ^, 끝은 $, \d에서 d는 digit(10진수)
    # http://www.regexr.com => 정규 표현식 배울 수 있는 사이트

# 정규 표현식 문법
    # 메타문자(meta-characters) : 문자를 설명하기 위한 문자, 원래의 의미가 아닌 다른 의미로 쓰임
        # 1. 기본 메타문자 []
            # '[' 와 ']' 사이의 문자와 매칭하라는 의미
                # ex) [abc] => 어떤 텍스트에 a or b or c라는 텍스트가 있는지 찾기
            # []에는 or의 의미도 있음
                # [Yy]esterday 라고 입력하면 yesterday, Yesterday 둘 다 한 번에 찾을 수 있음
            # 알파벳 or 한글 전체를 검색하고 싶으면 - 사용
                # [A-Za-z], [가-힝], [0-9]
        # 2. 반복 관련 메타문자 -, +, *, ?, {}
            # +는 해당 글자가 한 개 이상 출현한다는 것을 의미함
                # [0-9]+-[0-9]+-[0-9] (-는 대괄호 밖에서는 메타문자가 아님)
            # {}는 출현 횟수를 지정할 수 있음
                # [0-9]{3}-[0-9]{3,4}-[0-9]{4}  ({3,4}는 3자 또는 4자 출현 가능이라는 의미)
            # ?는 한 번만 반복한다는 것을 의미함
                # 01[016789]? 는 010, 011, 016, 017, 018, 019를 검색함
            # *는 {0,}을 의미하고, +는 {1,}을 의미함 (무한히 반복하는 것을 포함)
        # 3. 그 외 메타문자 (), ., |, ^, $, \
            # ()는 묶음을 의미, 메타문자의 묶음을 표시
                # 사용하지 않아도 되지만, 나중에 묶음으로 데이터를 받아 처리할 일이 있을 때 영역 설정 가능
            # .은 [.], (.)의 의미가 다름
                # [.]은 일반적인 마침표를 의미
                # (.)은 줄 바꿈 기호를 제외한 전체 문자를 의미
            # |은 or, ^은 not을 의미
                # [0|1] 과 같이 표현할 수 있지만, [01]이랑 의미가 같아 잘 쓰이지 않음
                # [0-9]{2}[^:][0-9] => 숫자 두 자리가 있고, 중간에 :이 없으며 다음에 숫자가 나오는 것만 출력
            # \는 메타문자를 찾고 싶을 때 사용
                # *를 찾고 싶으면 \* 를 쓰면 됨
        # 4. ^, $
            # ^ (대괄호 밖에 있는 메타문자)는 정규 표현식의 처음에 붙음
            # $는 정규 표현식의 끝에 붙음
            # 정규 표현식의 시작과 끝을 표현하는 메타문자
                # 꼭 붙이지 않아도 상관 없지만 많은 코드에서 붙인 것을 볼 수 있음