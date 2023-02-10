animal = ['Fox', 'DOg', 'Cat']
print([ani for ani in animal if 'o' not in ani])
# 'o'가 들어가기만 하면 조건 충족, 원소가 'o'만 있을 때가 아님
# 2차원 리스트라 생각하면 편할 듯
# 대문자는 당연히 조건 충족이 안 됨