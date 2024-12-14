INPUT_FILE = "2_input.txt"

def load_input(input_file: str) -> list:
	file = open(input_file, "r")
	input_arr = []	

	line = file.readline()
	while line != "":
		line = line.split()
		if (is_rising(line.copy()) or is_descending(line.copy())) and are_adjacent_levels_correct(line.copy()):
			# Note: All data remains str, need to int it before calculation
			input_arr.append(line)
		line = file.readline()

	# Good praxis to close file at end
	file.close()

	return input_arr

# Enter a line of numbers
def is_rising(line: list) -> bool:
	number = line.pop(0)
	tolerance_level = 1
	while line != []:
		# Left to right, rising numbers should give negative result each time
		# Otherwise, it's either the same next number or a lower
		if (int(number) - int(line[0])) >= 0:
			if tolerance_level < 1:
				return False
			else:
				tolerance_level -= 1

		number = line.pop(0)

	return True

# Enter a line of numbers
def is_descending(line: list) -> bool:
	number = line.pop(0)
	tolerance_level = 1
	while line != []:
		# Left to right, descending numbers should give positive result each time
		# Otherwise, it's either the same next number or a lower
		if (int(number) - int(line[0])) <= 0:
			if tolerance_level < 1:
				return False
			else:
				tolerance_level -= 1
		
		number = line.pop(0)

	return True

# Enter a line of numbers
def are_adjacent_levels_correct(line: list) -> bool:
	# Pop 0 since we are thinking from left to right of list, but doesn't matter in this case
	number = line.pop(0)
	tolerance_level = 1
	while line != []:
		# Requirement: Adjacent level must be an abs difference of between 1 and 3
		if 1 <= abs(int(number) - int(line[0])) <= 3:
			pass
		else:
			if tolerance_level < 1:
				return False
			else:
				tolerance_level -= 1

		number = line.pop(0)

	return True

safe_reports = load_input(INPUT_FILE)
amount_safe_reports = len(safe_reports)

test_case_bool = (is_rising([67,69,71,72,75,78,76]) or is_descending([67,69,71,72,75,78,76])) and are_adjacent_levels_correct([67,69,71,72,75,78,76])

print("The amount of safe reports, using a problem dampener, is:", amount_safe_reports)

print("Test case is:", test_case_bool)