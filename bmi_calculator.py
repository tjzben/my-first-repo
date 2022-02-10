firstName = input("What is your First Name: ")
lastName = input("What is your Last Name: ")
weight = float(input("What is your Weight in (KG): "))
height = float(input("What is your Height in (CM): "))

bmi_cal = weight / (height * height)

if bmi_cal < 18.5:
    print(f"Hi {firstName}, Risk of Nutritional Deficiency")
elif bmi_cal <23:
    print(f"Hi {firstName}, Low Risk")
elif bmi_cal < 27.5:
    print(f"Hi {firstName}, Moderate Risk")
else:
    print(f"Hi {firstName}, High Risk")
