bd_division = {}
bd_division["Barishal"] = {"district":6, 'upazila':39, 'council':333}
bd_division["Chittagong"] = {"district":11, 'upazila':97, 'council':336}
bd_division["Dhaka"] = {"district":11, 'upazila':97, 'council':336}
bd_division["Khulna"] = {"district":10, 'upazila':59, 'council':270}
bd_division["Mymensingh"] = {"district":4, 'upazila':34, 'council':350}
bd_division["Rajshahi"] = {"district":8, 'upazila':70, 'council':558}
bd_division["Rangpur"] = {"district":8, 'upazila':58, 'council':536}
bd_division["Sylhet"] = {"district":4, 'upazila':38, 'council':334}

print("Divisions are: ")
div = bd_division.keys()
for divs in div:
    print(divs)
print()
print("Upazilas are: ")
for divs in div:
    print(divs,"upazila =",bd_division[divs]["upazila"])
print()
print("printing all informations: ")
for all in div:
    print(all)
    print(bd_division[all])
