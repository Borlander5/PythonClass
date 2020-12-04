
with open('pi_digits.txt') as file_object:
	contents = file_object.read()



filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
