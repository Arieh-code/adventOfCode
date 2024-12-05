from collections import defaultdict
with open('input1.txt', 'r') as file:
    column1 = []
    column2 = []

    for line in file:
        num1, num2 = map(int, line.split())
        column1.append(num1)
        column2.append(num2)
        


# column1.sort()
# column2.sort()

# print(len(column1), len(column2))
# result = 0


# for left, right in zip(column1, column2):
#     result += abs(right - left)
        
# print(result)

rightMap = defaultdict(int)

for i in column2:
    rightMap[i] += 1
    
result = 0

for i in column1:
    result += (i * rightMap[i])
    
print(result)