weight = float(input("몸무게를 kg 단위로 입력하시오:"))
height = float(input("키를 미터 단위로 입력하시오:"))

Bmi = weight / (height**2)
print(f"당신의 BMI ={Bmi}")