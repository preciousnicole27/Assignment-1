num = [int(input(f"Enter numbers_{i+1} :")) for i in range(10)]
oddnum = sum(1 for n in num if n % 2 != 0)

print("number of odds:", oddnum)