name = "User1"

printableUsername = name
printableUsername = f"_{printableUsername}_"

print(name)
print(printableUsername)

inventory = ["меч", "яблоко"]

# | [меч] [яблоко] [] [] [] [] [] [] | <- область памяти
copyInventory = inventory   # invntory как ячейка, как переменная не может хранить другие ячейки, поэтому она хранит ссылку на область в памяти
copyInventory.append("золото")

print(inventory)
print(copyInventory)

# Копия
copyInventory = inventory[:]   # с какого до какого
copyInventory.append("золото")

print(inventory)
print(copyInventory)

map = [[".",".","."],
       [".",".","x"],
       [".","x","."]]

print(map[0][1])    # A(0,1)

# el - переменная в которую будут излекаться данные по очереди (какое хочешь название)
for el in map:  # справа от in должен стоять enumer-able тип (список или что-то на него похожее)
    for e in el:
        print(e, end="\t")
    print()
print()

for i in range(0, len(map)):   #range дает тебе список от 0 до 3 (3 не включая)
    for j in range(0,len(map[i])):
        print(map[i][j], end= "\t")
    print()

print(map[-1])