class phone:
    def __init__(self):
        print("from phone class ")

class redmi(phone):
    def __init__(self):
        super().__init__()
        print("from redmi class")

p = phone()
r = redmi()
