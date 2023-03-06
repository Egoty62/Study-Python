from . import series
from . import statics
# from . 을 붙이는 이유 : 현재 디렉터리인 analysis의 패키지를 호출하기 위해
    # 붙이지 않으면 상위 디렉터리인 roboadviser에서 series나 statics 패키지를 찾게 돼 오류 발생
        # 마찬가지로 여기에서 이 파일을 컴파일하면 오류 발생
            # ImportError: attempted relative import with no known parent package
__all__ = ['series', 'statics']