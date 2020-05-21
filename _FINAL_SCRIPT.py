import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--script', default=f'_13_sentence_score_combined.txt', required=False, type=str,
					help='test in')
parser.add_argument('-o', '--output', default=f'_FINAL_SCRIPT.txt', required=False, type=str,
					help='test out')

args = parser.parse_args()

script_pattern = re.compile(r'^(?P<script>.*?)(=)(?P<score>.*?)\n*$')

script_list = []

with open(args.script, 'r', encoding='utf-8') as rf:

	for line in rf.readlines():
		m = script_pattern.search(line)
		script = m.group('script')
		score = m.group('score')
		script_tuple = (score, script)
		script_list.append(script_tuple)

	script_list.sort(reverse=True)

with open(args.output, 'w', encoding='utf=8') as wf:
	for score,script in script_list:
		wf.writelines(str(script)+'\n')
