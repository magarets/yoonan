Fahrenheit = int(input("화씨 온도를 입력하시오: ")) # 화씨 온도
Celsius = (Fahrenheit - 32) * float(5/9) # 섭씨온도 계산
print(f"화씨 {Fahrenheit}도는 섭씨", "%.2f" % Celsius, "도에 해당합니다.")