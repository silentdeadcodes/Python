rows = int(input("Amount of rows: "))
columns = int(input("Amount of columns: "))
symbol = input("Symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


