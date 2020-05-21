
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=f'_0_dictionary_sentence_set.txt', required=False, type=str,
                    help='test in')
parser.add_argument('-o', '--output', default=f'_1_dictionary_seperate_dash.txt', required=False, type=str,
                    help='test out')

args = parser.parse_args()

pattern = re.compile(r'^(?P<text>.*?)\n*$')

heteronym_list = []
line_list = []

with open(args.input, 'r', encoding='utf-8') as rf:
    for line in rf.readlines():
        m = pattern.search(line)
        text = m.group('text')

        text = re.findall(r'[가-힣]+', text)

        dash = "-"
        text = ' '.join(text)
        text = ' '.join(text)
        text = re.sub(' ', '-', text)
        text = re.sub('---', ' ', text)

        line_list.append('{}\n'.format(text))

with open(args.output, 'w', encoding='utf=8') as wf:
    wf.writelines(line_list)