import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=f'_3_dictionary_frequency.txt', required=False, type=str,
					help='test in')
parser.add_argument('-o', '--output', default=f'_4_diphone_dictionary.txt', required=False, type=str,
					help='test out')

args = parser.parse_args()

pattern = re.compile(r'^(\()(?P<count>.*?)(\, \')(?P<text>.*?)(\'\))\n*$')

heteronym_list = []
line_list = []

with open(args.input, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = pattern.search(line)
		count = m.group('count')
		text = m.group('text')

		line_list.append('{}  {}\n'.format(text, count))

with open(args.output, 'w', encoding='utf=8') as wf:
	wf.writelines(line_list)