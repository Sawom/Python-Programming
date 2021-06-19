class laptop:
    brand = ''
    ram = ''
    rom = ''

asus = laptop()
print(isinstance(asus,laptop))
asus.brand = 'asus'
asus.ram = '8 gb'
asus.rom = '512 gb'


print(f" brand = {asus.brand}, ram = {asus.ram}, rom = {asus.rom} ")
