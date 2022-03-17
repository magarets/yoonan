Num = int(input("정수="))
Total = 0 # 뗀 정수를 저장하는 변수 초기화
X = 10 # default
for i in range(4):
    Total += Num % X
    Num //= 10

print(Total)