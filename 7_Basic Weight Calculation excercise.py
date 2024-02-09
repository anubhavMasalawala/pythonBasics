weight = int(input("Enter your weight? "))
unit = input("(K)gs or (L)bs ")

if unit.upper() == str("K") :
    print("Your weight in lbs : "+str(weight*2.20462))
elif unit.upper() == str("L"):
    print("Your weight is kgs : "+str(weight/2.20462))