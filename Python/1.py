# https://adventofcode.com/2024/day/1

INPUT_FILE = "1_input.txt"

# Will append values while reading file
left_list = []
right_list = []
# Holds the total distance, can add distance for each # directly
total_distance = 0

similarity_score = 0

f = open(INPUT_FILE, "r")
line = f.readline()
while line != "":
    left_list.append(line.split()[0])
    right_list.append(line.split()[1])
    line = f.readline()

# Good praxis to close file after usage
f.close()

# By sorting, we can use the same element for both lists when calculating distance
left_list.sort()
right_list.sort()

# Use abs in case of negative sum
for i in range(len(left_list)):
    total_distance += abs(int(left_list[i]) - int(right_list[i]))

for i in left_list:
    amount = 0
    for j in right_list:
        if i == j:
            amount += 1
    similarity_score += amount * int(i)

print("The total distance is:", total_distance)
print("The similarity score is:", similarity_score)