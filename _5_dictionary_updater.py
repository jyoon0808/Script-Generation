import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base', default=f'_0_diphone_base.txt', required=False, type=str,
					help='test in')
parser.add_argument('-i', '--input', default=f'_4_diphone_dictionary.txt', required=False, type=str,
					help='test in')
parser.add_argument('-o', '--output', default=f'_5_dictionary_updated.txt', required=False, type=str,
					help='test out')

args = parser.parse_args()

base_pattern = re.compile(r'^(?P<diphone>.*?)\n*$')
input_pattern = re.compile(r'^(?P<diphone>.*?)(  )(?P<count>.*?)\n*$')

base_list = []
input_list = []
totals_list = []

with open(args.base, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = base_pattern.search(line)
		diphone = m.group('diphone')
		base_list.append('{}'.format(diphone))

with open(args.input, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = input_pattern.search(line)
		diphone = m.group('diphone')
		count = m.group('count')
		input_list.append('{}'.format(diphone))
		totals_list.append('{}  {}\n'.format(diphone,count))
		print(totals_list)
diff_list = list(set(base_list) - set(input_list))

for diff in diff_list:
	totals_list.append('{}  1\n'.format(diff))

with open(args.output, 'w', encoding='utf=8') as wf:
	wf.writelines(totals_list)
