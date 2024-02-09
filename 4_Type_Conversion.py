# Type conversion
    # int() - convert value to integer
    # float() - convert value to float
    # bool() - convert value to boolean
    # string() - convert value to string

birthYear = input("What is your birth year? ") # Return String

age = 2023 - int(birthYear) # conversion of string to integer to subtract year

print(age)

# integer to float conversion

unit = float(age)
print(unit)