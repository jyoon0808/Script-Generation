import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--script', default=f'_6_unnecessary_deleted.txt', required=False, type=str,
					help='test in')
parser.add_argument('-i', '--score', default=f'_12_sentence_score.txt', required=False, type=str,
					help='test in')
parser.add_argument('-o', '--output', default=f'_13_sentence_score_combined.txt', required=False, type=str,
					help='test out')

args = parser.parse_args()

script_pattern = re.compile(r'^(?P<script>.*?)\n*$')
score_pattern = re.compile(r'^(?P<score>.*?)\n*$')
total_pattern = re.compile(r'^(?P<script>.*?)(  )(?P<score>.*?)\n*$')

script_list = []
score_list = []
text_list = []

with open(args.script, 'r', encoding='utf-8') as rf:
	for aline in rf.readlines():
		m = script_pattern.search(aline)
		script = m.group('script')
		script_list.append('{}'.format(script))

with open(args.score, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		m = score_pattern.search(line)
		score = m.group('score')
		score_list.append('{}'.format(score))


def a(num):
	for x in num:
		yield x

x1 = a(script_list)
x2 = a(score_list)

for i,j in zip(x1,x2):
	text_list.append('{}''=''{}''\n'.format(i,j))

with open(args.output, 'w', encoding='utf=8') as wf:
	wf.writelines(text_list)
