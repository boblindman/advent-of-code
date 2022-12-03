# Advent of Code 2022 - Day 1
  
# Using readlines()
file1 = open('Day1-AdventOfCode-Input.txt', 'r')
Lines = file1.readlines()
  
count = 0
sum = 0
maxSum = 0

# Strips the newline character
for line in Lines:
    count += 1
    stringValue = line.strip()
    if len(stringValue) < 1:
        if sum > maxSum:
                maxSum = sum
        print("Line{}: {}".format(count, sum))
        sum = 0
    else:
        sum += int(line.strip())

print("Max Sum = {}".format(maxSum))