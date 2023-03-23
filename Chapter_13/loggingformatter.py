# 로그의 결과값을 일정 형식을 지정하여 출력하는 기능

import logging

logger = logging.getLogger('myapp')     # Logger 생성
hdlr = logging.FileHandler('myapp.log') # FileHandler 생성

formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s') # s는 문자열, d는 정수형
# Logging Formatter 생성 : 시간, 로깅 레벨, 프로세스 ID, 메세지
hdlr.setFormatter(formatter)    # FileHandler에 formatter 등록
logger.addHandler(hdlr)         # Logger에 'FileHandler' 등록
logger.setLevel(logging.INFO)   # 로깅 레벨 설정

logger.error('ERROR occurred')  # 로깅 정보 출력
logger.info('HERE WE ARE')
logger.info('TEST finished')

# 11, 12행에서 생성된 객체를 Logger 객체에 등록
    # 먼저 Handler 객체에 Formatter 객체를 등록
        # Logger 객체에서 Handler를 등록
            # 12행에서 로깅 레벨을 설정