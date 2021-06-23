def voter(age):
    if age < 18:
        raise Exception("invalid voter. Under 18...")
    return "you are selected!"

try:
    age = int(input("Enter age: "))
    result = voter(age)
    print(result)

except Exception  as e:
    print(e)