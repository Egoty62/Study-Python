# 웹은 1989년 물리학자인 팀 버너스 리(Timothy Berners Lee)가 개발
# 웹을 개발한 원래 목적은 물리학자들이 편하게 여러 정보를 교환하기 위해서였음

# 웹은 다양한 컴포넌트로 이루어져 있음 => 중요한 컴포넌트는 HTML, HTTP
    # 1. HTML(Hyper Text Markup Language)
        # 웹상의 정보를 구조적으로 표현하기 위한 언어
            # 웹에서는 일종의 신문처럼 여러 정보를 구조적으로 표현
                # ex) 제목, 단락, 다른 신문 기사와 연결된 링크 등
        # 이런 구조 정보를 태그(tag)라는 개념을 사용하여 표현한 것이 HTML
        # 태그는 '<>'로 둘러싸여있고, 그 안에 정보에 대한 의미 작성 후 끝나는 부분에 슬래시를 사용해 해당 태그 종료
            # <title> Hello, World </title>
    # 2. HTTP(Hypertext Transaction Protocol)
        # 인터넷에서 컴퓨터 간 정보를 주고받을 때 사용하는 일종의 약속
            # 일반적으로 컴퓨터 과학에서 이런 약속을 프로토콜(Protocol)이라 함
        # 일종의 텍스트 데이터 교환
            # 컴퓨터 간에 정보를 주고받을 때는 HTML을 주고받을 때 필요한 다양한 정보를 주고받는 포맷을 사전에 정의
                # 어떤 컴퓨터가 접속하는지, 어떤 운영체제를 사용하는지, 언제 접속했는지, 문서의 제목이 무엇인지 등
        # 최근에는 보안 문제때문에 HTTPS(Hypertext Transfer Protocol Secure)를 주로 사용
    # 이외에도 FTP, SSH 등이 있음

# 웹의 동작 순서
    # http://www.domain.com/1234/path/to/resource?a=b&x=y
        # http : protocol
        # www.domain.com : host
        # 1234 : port
        # path/to/resource : resource path
        # ?a=b&x=y : query
    # 웹 브라우저에 접속하여 URL 주소 입력
        # URL 주소에 포함된 도메인 네임을 찾게 됨
            # 그 도메인 네임의 IP주소를 도메인 네임 서버(DNS)를 통해 알아냄
                # 이후 해당 IP주소를 가진 서버에 접속해 필요한 정보를 요청

# 웹 스크래핑
    # 모든 웹은 HTML로 구성되어 있음
        # HTML의 규칙을 파악한다면 필요한 정보를 가져올 수 있는데, 이를 웹 스크래핑이라 함
            # 웹 크롤링(crawling) : 웹에서 문서를 긁어 가져오는 과정
            # 웹 스크래핑(scrapping) : 가져온 문서에서 필요한 정보를 추출하는 과정
                # 국내에서는 비슷한 의미로 사용됨