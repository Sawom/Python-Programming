class student:
    name = ''
    roll = ''
    gpa = ''
    section = ''
    gender = ''


sawom = student()
print(isinstance(sawom,student))
sawom.name = 'sawom'
sawom.roll = 1012
sawom.gpa = 3.51
sawom.section = 'A'
sawom.gender = 'male'
print(f"name = {sawom.name},roll = {sawom.roll}, gpa= {sawom.gpa}, section = {sawom.section}, gender = {sawom.gender} \n")

maliha = student()
print(isinstance(maliha,student))
maliha.name = 'maliha'
maliha.roll = 1013
maliha.gpa = 3.81

maliha.section = 'A'
maliha.gender= 'female'
print(f"name = {maliha.name},roll = {maliha.roll}, gpa= {maliha.gpa}, section = {maliha.section}, gender = {maliha.gender} \n")