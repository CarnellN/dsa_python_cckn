print("Hello Python!")

name = "Paul"
name2 = 'Paul'
num = 10
balance = 100.50
flag = True

print(id(name))
print(id(name2))
print(type(num))
print(type(balance))
print(type(flag))

for i in range(1, 11):
    if i % 2 == 0:
        print(i)