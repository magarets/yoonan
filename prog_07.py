x1 = int(input()) # x1
y1 = int(input()) # y1
x2 = int(input()) # x2
y2 = int(input()) # y2

Distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 # 거리 계산, 루트를 씌우기 위해 0.5를 제곱함

print(f"두점 사이의 거리: {Distance}")