animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs = [4, 0, 2, 4, 8]
animal_leg_dict = {}

for i in range(len(animal)) :
    animal_leg_dict[legs[i]] = animal[i]    # for 문이라 key의 숫자가 겹치는 4는 'ant'로만 저장됨

animal_leg_dict['ant'] = 6

print(animal_leg_dict)  # {4 : 'ant', 0 : 'snake', 2 : 'monkey', 8 : 'spider', 'ant' : 6}