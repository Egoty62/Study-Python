# from .analysis import series
# import analysis
# import crawling
# import database
from . import analysis
import roboadviser.crawling
import roboadviser.database

__all__ = ['analysis', 'crawling', 'database']

# 현재 파일에서는 오류가 발생함
# 하지만 roboadviser의 상위 디렉터리에 있는 'package.py'파일에서 이 파일을 원활하게 실행 가능
# line 1, 2의 경우에는 현재 파일에서는 컴파일이 가능함
    # 하지만 상위 디렉터리에서 하위 디렉터리의 모듈을 가져올 때 오류가 발생
    # 따라서 상위 디렉터리에서 이 파일을 호출할 때 절대참조를 하는 것이 편해보임
        # 이 메인 init 파일과 동일 경로에 있는 파일에서 모듈을 불러올 경우 line 2~4 처럼 하면 됨

# ==========================================================================================================================================
# 이 init 파일을 통해 모듈을 불러오는 메인 파일의 경로가 어디인지 따라서 코드가 살짝씩 바뀔 것 같음
# ==========================================================================================================================================