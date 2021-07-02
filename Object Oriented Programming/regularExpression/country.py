s = "Afganisthan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, switzerland"
countries = s.split(",")
print(countries)
#li = [item for item in countries if item.endswith("land") or item.endswith("lands")]
print("ends with land or lands = ")
for i  in countries:
    if i.endswith("land") or i.endswith("lands"):
        print(i)
