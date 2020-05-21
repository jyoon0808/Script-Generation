import math
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--input", default='_11_calculation_dividend.txt', required=False, type=str,
					help='input file')
parser.add_argument('-d', "--div", default='_10_sentence_length.txt', required=False, type=str,
					help='input file')
parser.add_argument('-o', '--output', default='_12_sentence_score.txt', required=False, type=str,
					help='output file name')

args = parser.parse_args()
pattern = re.compile(r'^(?P<number>.*?)\n*$')
prediv_list = []
divisor_list = []
sentence_score_list = []

with open(args.input, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = pattern.search(line)
		prediv_score = m.group('number')
		prediv_list.append(float(prediv_score))

with open(args.div, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		line = re.findall(r'[\'][ㄱ-ㅎㅏ-ㅣ ][\']', line)
		divisor_list.append(float(len(line)))

for p, d in zip(prediv_list, divisor_list):
	if d >= 80:
		if d != 0 and d != 1:
			print(f'{p} divided by log of {d} = {p/math.log(d)}')
			sentence_score_list.append(p/math.log(d))
		else:
			d = 1 + 1e-10
			print(f'{p} divided by log of {d} = {p/math.log(d)}')
			sentence_score_list.append(p/math.log(d))
	else:
		sentence_score_list.append(0)



with open(args.output, 'w', encoding='utf-8') as wf:
	for score in sentence_score_list:
		wf.writelines(str(score) + '\n')

