weight=float(input("Enter your weight in (kgs): "))
height=float(input("Enter your height in (m): "))
bmi=(weight)/(height**2)
print(bmi)
if bmi>28:
    print("obese")
elif bmi>25:
    print("Over weight")
elif bmi>18:
    print("Normal weight")
else:
    print("Under weight")