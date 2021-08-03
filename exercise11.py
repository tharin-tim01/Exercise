row = int(input("How many floor in this pyramid: "))
y = 1
for i in range(row):
    print (" " * (row - i) + "*" * y)
    y = y + 2