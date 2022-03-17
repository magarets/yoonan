x = 10
y = 20
print(f"두수의 합: {x+y}")
print(f"두수의 차: {x-y}")
print(f"두수의 곱: {x*y}")
print(f"두수의 평균: {(x+y)/2}")
print("큰수 : ", end="")
if x > y:
    print(x)
    print(f"작은수 : {y}")
else:
    print(y)
    print(f"작은수 : {x}")
