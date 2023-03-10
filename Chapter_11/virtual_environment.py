# 파이썬을 하다보면 자신이 직접 만든 프로그램보다 다른 사람이 만든 프로그램을 가져와 사용하는 경우가 더 많음
# 한 번에 하나가 아닌 2개 이상의 프로젝트를 진행하게 된다면 각 프로젝트에 맞는 프로그래밍 환경을 설정하는 것이 좋음
    # 데이터를 다루는 프로젝트, 웹을 다루는 프로젝트는 성격이 다름 => 각 프로젝트에 맞는 환경을 설정 후 진행해야 함

# 파이썬에서 이런 경우를 지원하기 위해 가상환경이라는 개념으로 프로젝트의 패키지를 관리하는 도구 제공
    # 일반적으로 어떤 프로젝트를 수행할 때 파이썬 코드를 수행할 기본 인터프리터에서 추가로 프로젝트별 필요한 패키지를 설치
        # 이러한 패키지를 설치할 때 서로 다른 프로젝트가 영향을 받지 않도록 독립적인 프로젝트 수행 환경을 구성 (가상환경)
            # 이 가상환경을 구축하기 위해 패키지 관리 도구를 사용

# 대표적인 가상환경 도구로 virtualenv, conda가 있음
    # virtualenv는 파이썬에서 기본으로 제공하는 가상환경 도구
        # pip를 이용해 새로운 패키지를 설치 가능
    # conda는 본 책에서 사용하는 인터프리터인 miniconda의 전용 패키지 관리 도구
    # 일반적으로 virtualenv와 pip를 같이 사용하여 새로운 패키지를 설치할 것을 권장
        # 파이썬 패키지는 대부분 파이썬 코드뿐 아니라 C코드를 같이 설치할 때가 많아 컴파일 된 C파일을 설치해야 함
            # pip는 이를 지원하지 않을 때가 많음

# 본 책에서는 conda를 사용하여 가상환경을 다루지만, 본인은 vscode를 다루고 있으므로 책과는 다르게 공부함
    # 참고 : https://it4edu.tistory.com/160

# 터미널을 통해 가상환경을 만들기
    # 1. ctrl + ` 를 통해 터미널로 이동
    # 2. 'python -m venv "생성할 폴더 이름" (폴더 위치 설정하기)
    # 3. 가상환경에서 사용할 인터프리터 설정
        # F1 또는 Ctrl + Shift + P 후 Python Select Interpreter입력
            # 그 후 미리 만들었던 가상환경 폴더 선택
    # 4. 터미널 화면 우상단 + 버튼 클릭
        # 새 터미널이 실행됨 (이게 가상환경 설정)
    # 5. 가상환경 내에서 원하는 라이브러리 설치
        # 여기에서는 matplotlib 설치
            # pip install matplotlib

# 가상환경은 활성화 된 이후 비활성화 되기전까지 유지됨
    # 다른 프로젝트로 가기전에 꼭 비활성화 해줘야 함
        # 비활성화 방법은 가상환경 폴더의 Script폴더 내에 deactivate.bat파일 실행
            # 위 방법 보다는 터미널에 deactivate 입력이 나음

# 가상환경 설정 테스트
import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(10)]
y = [i ** 2 for i in x]
plt.plot(x, y, 'ko-', label = 'function')
plt.ylabel('matplotlib practice')
plt.legend()
plt.grid()
plt.show()