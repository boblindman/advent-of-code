# Advent of Code 2022 - Day 1
  
# Using readlines()
file1 = open('Day1-AdventOfCode-Input.txt', 'r')
Lines = file1.readlines()
  
count = 0
sum = 0
maxSum1 = 0
maxSum2 = 0
maxSum3 = 0

# Strips the newline character
for line in Lines:
    count += 1
    stringValue = line.strip()
    if not len(stringValue):
        if sum > maxSum1:
                maxSum3 = maxSum2
                maxSum2 = maxSum1
                maxSum1 = sum
        elif  sum > maxSum2:
                maxSum3 = maxSum2
                maxSum2 = sum
        elif sum > maxSum3:
                maxSum3 = sum
        #print("Line{}: {}".format(count, sum))
        sum = 0
    else:
        sum += int(stringValue)

print("Max Sum = {} + {} + {}  = {}".format(maxSum1,maxSum2,maxSum3,maxSum1+maxSum2+maxSum3))