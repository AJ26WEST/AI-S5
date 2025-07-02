
with open('numbers.csv', 'r') as file:
    lines = file.readlines()


numbers = [int(line.strip()) for line in lines]


numbers.sort()

print("Sorted numbers:")
for num in numbers:
    print(num)
