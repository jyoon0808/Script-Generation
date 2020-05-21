import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=f'_0_original_text.txt', required=False, type=str,
                    help='test in')
parser.add_argument('-o', '--output', default=f'_6_unnecessary_deleted.txt', required=False, type=str,
                    help='test out')

args = parser.parse_args()

pattern = re.compile(r'^(?P<text>.*?)\n*$')

line_list = []

with open(args.input, 'r', encoding='utf-8') as rf:
    for line in rf.readlines():
        m = pattern.search(line)
        text = m.group('text')

        text = re.findall(r'[가-힣]+', text) # get rid of all the characters other than Korean
        text = ' '.join(text) # converting list to string

        text = re.sub(r'(.|.[ ]|..|..[ ]|...|...[ ])\1{2,}','',text) # get rid of all the repetitions of words and characters

        line_list.append('{}\n'.format(text))

with open(args.output, 'w', encoding='utf=8') as wf:
    wf.writelines(line_list)