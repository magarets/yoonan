Chicken = int(input("닭의 수")) # 닭의 마리 수
Pig = int(input("돼지의 수")) # 돼지의 마리 수
Cow = int(input("소의 수")) # 소의 마리 수

Total = Chicken * 2 + Pig * 4 + Cow * 4 # 총 다리의 합, 닭:2 돼지:4 소:4
print(f"전체 다리의 수: {Total}")