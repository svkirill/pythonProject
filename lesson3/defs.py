# y = 2x + 3
# x 0
# y 3

# f(x) => y

def calc(x):
    result = 2*x + 3
    return result

def print_fullname(name, surname):
    print(f"Fullname: {name} {surname}")

x0 = 0
res = calc(x0)
print(res)

print_fullname("Ivan", "Ivanov")