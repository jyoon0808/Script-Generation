import re
import math
def Dict2ListDecorator(func):
	def Dict2List(my_list):
		my_input = func(my_list)
		my_output = []
		for key, value in my_input.items():
			key_value = f'{key}:{value}\t'
			my_output.append(key_value)
		return my_output
	return Dict2List

@Dict2ListDecorator
def CountFrequency(my_list):
	# Creating an empty dictionary
	freq = {}
	for word in my_list:
		freq[word] = freq.get(word, 0) + 1
	return freq

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', "--totals", default='_5_dictionary_updated.txt', required=False, type=str,
					help='input key')
parser.add_argument('-c', "--counts", default='_9_diphone_count.txt', required=False, type=str,
					help='input file')
parser.add_argument('-o', '--output', default='_11_calculation_dividend.txt', required=False, type=str,
					help='output file name')
args = parser.parse_args()



dp_totals = {} #
dp_list = []
# pattern = re.compile(r'[ㄱ-ㅎ][-][ㄱ-ㅎ]|[ㄱ-ㅎ][-][ㅏ-ㅣ]|[ㅏ-ㅣ][-][ㄱ-ㅎ]')
totals_pattern = re.compile(r'^(?P<diphone>.*?)(  )(?P<total>.*?)\n*$')
counts_pattern = re.compile(r'^(?P<text>.*?)\n*$')
with open(args.totals, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = totals_pattern.search(line)
		diphone = m.group('diphone')
		count = m.group('total')

		dp_totals[diphone] = int(count)	#assign totals to each diphone
		dp_list.append(diphone) #list of diphones
#now we have a key value list for TOTALS

line_list = []
output_list = []


key_value_list = []

with open(args.counts, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = counts_pattern.search(line)
		text = m.group('text')

		key_values = re.findall(r'[^\t\n]+', text)

		key_value_list.append(key_values)
#
# for key_value in key_value_list:
# 	key_value_dict = {}

score_list = []
for key_value in key_value_list:
	n = 0
	score = 0
	temp_d = {}
	for pair in key_value:
		key, value = pair.split(':')
		temp_d[key] = int(value)


	for key, value in temp_d.items():
		n += value
		if value == 1:
			score += -math.log(value/dp_totals[key])
		else:
			for i in range(value):
				score += -math.log(1/dp_totals[key])

	print(f'score: {score}, n: {n}')
	if n != 0:
		score_list.append(score/n)
	else:
		score_list.append(0)

with open(args.output, 'w', encoding='utf-8') as wf:
	for score in score_list:
		wf.writelines(str(score) + '\n')