# XML(eXtensible Markup Language) : 확장적인 마크업 언어
    # 데이터의 구조와 의미를 설명하는 태그를 사용해 어떤 데이터의 속성과 값을 표현하는 언어
    # 시작태그와 종료 태그 사이에 어떤 값이 있음
        # 그 값은 태그의 이름으로 만들어진 속성에 대한 값이 됨
    # HTML과 비슷함
        # HTML은 XML에서 웹에 필요한 개념만 정의하여 사용가능하게 만들어진 언어
    # HTML과는 달리 다양한 형태로 데이터를 표현할 수 있음

# XML의 구조
    # 교재에 있는 내용을 그대로 가져왔음
    # <?xml version="1.0"?>
    # <학생>
        # <이름>한재일</이름>
        # <학번>20105503</학번>
        # <나이>26</나이>
        # <학과>산업경영공학과</학과>
        # <성별>남성</성별>
    # </학생>

    # 이러한 구조는 class, object 개념과 크게 다르지 않음
    # 딕셔너리 형태로도 바꿔 표현 가능

# XML 문서
    # XML로 정보를 표현할 때 가장 기본적인 방법은 트리(tree)형태로 표현하는 것
        # HTML과 완전히 같음, 모든 태그 기반의 언어가 지닌 공통적 특징
    # <?xml version="1.0"?>
        # <books>
            # <book>
                # <author>Carson</author>
                # <price format="dollar">31.95</price>
                # <pubdate>05/01/2001</pubdate>
            # </book>
            # <pubinfo>
                # <publisher>MSPress</publisher>
                # <state>WA</state>
            # </pubinfo>
        # </books>

    # 딕셔너리로 표현 가능
        # {books : [{book : {author : Carson, price : 31.95, pubdate : 05/01/2001]}

# JSON(JavaScript Object Notation) : 자바스크립트의 데이터 객체 표현 방식을 사용해 데이터 교환의 표준으로 삼은 데이터 표현 언어
    # 간결한 특성 때문에 기계와 인간 모두가 이해하기 쉬움
    # XML보다 데이터 용량이 적고 코드로의 전환이 쉬움
        # XML의 대체재로 가장 많이 활용됨
    # JSON은 딕셔너리형과 매우 비슷함
# {
    # "dataTitle":"JSON Tutorial!",
    # "swiftVersion":2.1

    # "users":[
        # {
            # "name":"John",
            # "age":25
        # },
        # {
            # "name":"Mark",
            # "age":29
        # },
        # {
            # "name":"Sarah",
            # "age":22
        # }
    # ],
# }

# user라는 키에는 값으로 리스트형이 있고, 그 안에 name과 age라는 2개의 키가 또 하나의 딕셔너리 형으로 있음

# JSON과 XML
    # 공통점
        # 데이터 구조가 기본적으로 트리(tree)구조
            # XML, JSON 모두 요소 간의 포함 관계를 가짐
        # 태그를 사용하여 키와 값을 구분한 XML처럼 JSON은 키-값 쌍으로 데이터 구조화 가능
    # 비교할 점
        # JSON은 XML에 비해 코드가 간결하고, 코드의 전환이 쉬움
            # 용량 절약이 용이