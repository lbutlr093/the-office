import csv
from collections import defaultdict

speaker_dict = {}
with open('the_office_lines.csv', 'r') as lines_file:
	office_reader = csv.reader(lines_file, delimiter = ',')
	header = office_reader.next()
	for row in office_reader:
		character = row[5]
		if character not in speaker_dict:
			speaker_dict[character] = 1
		else:
			speaker_dict[character] += 1
## top 5 characters sorted
sorted_speaker_dict = sorted(speaker_dict, key = speaker_dict.get, reverse = True)[:5]
for item in sorted_speaker_dict:
	print(str(item) + ': ' + str(speaker_dict[item]))