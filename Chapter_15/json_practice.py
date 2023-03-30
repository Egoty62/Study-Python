import json

dict_data = {'fruit' : 'lime'}
another_dict_data = {"fruit2" : "lemon", "fruit3" : 'apple'}

with open("practice.json", "w") as f :
    json.dump(dict_data, f)

# with open("practice.json", "a") as h :    # json 파일에서는 최상위 목록 하나만 포함됨
    # json.dump(another_dict_data, h)       # 때문에 이런 식으로 이어 붙히면 읽을 때 오류가 남

with open("practice.json", "r", encoding="utf8") as g :
    contents = g.read()
    json_data = json.loads(contents)
    print(json_data["fruit"])