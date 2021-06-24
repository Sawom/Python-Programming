class phone:
    def call(self):
        print("You can call ")

    def message(self):
        print("You can message")

class redmi(phone):
    def camera(self):
        print("camera is 48 mega pixel")

print("for phone class")
ph = phone()
ph.call()
ph.message()
print()
print("for redmi class")
r = redmi()
r.call()
r.message()
r.camera()