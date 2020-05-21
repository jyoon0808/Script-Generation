import re

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
parser.add_argument('-i', "--input", default='_8_korean_in_diphone.txt', required=False, type=str,
					help='input file')
parser.add_argument('-o', '--output', default='_9_diphone_count.txt', required=False, type=str,
					help='output file name')
args = parser.parse_args()


pattern = re.compile(r'^(?P<text>.*?)\n*$')
line_list = []
output_list = []
with open(args.input, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = pattern.search(line)
		text = m.group('text')

		list_of_words = re.findall(r'[ㄱ-ㅎ][-][ㄱ-ㅎ]|[ㄱ-ㅎ][-][ㅏ-ㅣ]|[ㅏ-ㅣ][-][ㄱ-ㅎ]+', text)

		line_list.append(list_of_words)

with open(args.output, 'w', encoding='utf-8') as wf:
	for line in line_list:
		x = CountFrequency(line)
		x = ''.join(x)
		wf.writelines(x + '\n')