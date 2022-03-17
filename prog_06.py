FoodCost = int(input("음식 비용: ")) # 음식비용
Tip = int(input("팁 비율: ")) # 팁
TipCost = FoodCost * float(Tip / 100) # 팁 : 음식값 / 팁 비율
TotalCost = int(FoodCost + TipCost) # 총 금액 : 음식값 + 팁 비용

print(f"총액: {TotalCost}달러")

