import logging
import logging.config
import csv

# 모듈 호출
logging.config.fileConfig('logging.conf')   # Logger 생성
logger = logging.getLogger()

bupyeong_list = []
bupyeong = None

# 변수 선언 등 생략
logger.info('Open file {0}'.format('TEST',))    # 이 이후로 format()에 다 tuple이 들어가는데, 상관 없을 것 같아서 그냥 , 뺐음
try :
    with open("인천광역시_유동인구_202110.csv", 'r', encoding = 'cp949') as f :
        reader = csv.reader(f, delimiter = ',', quotechar = '"')
        for citizen in reader :
            if citizen[7] == "삼산동" :     # 아무 동네나 넣어도 됨(부평동, 갈산동 등)
                logger.info('{0} 유동인구 추가됨'.format(citizen[7]))
                bupyeong_list.append(citizen)

except FileNotFoundError as e :
    logger.error("File not found {0}".format(e))

logger.info("삼산 유동인구의 데이터를 {0}에 적는 중".format('samsan_floating_population_data.csv"'))
with open("samsan_floating_population_data.csv", "w") as g :
    for population in bupyeong_list :
        g.write(",".join(population).strip('\n') + "\n")

logger.info("프로그램 종료")

# 데이터가 너무 많아서 로그 따는 데만 몇 분이 걸림...