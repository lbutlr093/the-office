import re
import csv
from collections import defaultdict

speaker_dict = {}			#Speakers, and how many lines they each have
speaker_appear = {}			#which season each speaker appears in
with open('the_office_lines.csv', 'r') as lines_file:
	office_reader = csv.reader(lines_file, delimiter = ',')
	header = office_reader.next()
	for row in office_reader:
		dialog = re.sub(r'[^\x00-\x7f]',r'', row[4]).replace('_', '')		#cleaning dialog
		#dialog					#each line of dialog
		character = row[5]		#the character that speaks each line of dialog
		if character not in speaker_dict:
			speaker_dict[character] = 1
			speaker_appear[character] = row[1]
		else:
			speaker_dict[character] += 1

## top 25 characters sorted
sorted_speaker_dict = sorted(speaker_dict, key = speaker_dict.get, reverse = True)[:25]
print('Top 25 characters with the most lines of dialog')
for item in sorted_speaker_dict:
	print(str(item) + ': ' + str(speaker_dict[item]))