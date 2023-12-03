numbers = []
answers = []

file1 = open('day1.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    for i in line.strip():
        if i.isdigit():
            numbers.append(i)

    if len(numbers) == 1:
        answers.append(int(numbers[0] + numbers[0]))
    else:
        answers.append(int(numbers[0] + numbers[- 1])) 
    numbers.clear()

total = sum(map(int, answers))

print(total)
    
    





