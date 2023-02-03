dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}

dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())

dict_2 =dict()

for i in range(len(dict_keys)) :
    dict_2[dict_values[i]] = dict_keys[i]   # list와는 표기 방식이 다름
                                            # dict[key]로 출력하면 key에 해당되는 value가 출력됨
print(dict_2[6])    # 10