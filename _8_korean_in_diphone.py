import re
from jamo import j2hcj as un
from jamo import h2j as wrap
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default=f'_7_korean_with_dash.txt', required=False, type=str,
                    help='test in')
parser.add_argument('-o', '--output', default=f'_8_korean_in_diphone.txt', required=False, type=str,
                    help='test out')

args = parser.parse_args()

pattern = re.compile(r'^(?P<text>.*?)\n*$')

heteronym_list = []
line_list = []

with open(args.input, 'r', encoding='utf-8') as rf:
    for line in rf.readlines():
        m = pattern.search(line)
        text = m.group('text')
        text = un(wrap(text))
        text = re.findall(r'[ㄱ-ㅎ][-][ㄱ-ㅎ]|[ㄱ-ㅎ][-][ㅏ-ㅣ]|[ㅏ-ㅣ][-][ㄱ-ㅎ]', text)

        text = ' '.join(text)
        line_list.append('{}\n'.format(text))

with open(args.output, 'w', encoding='utf=8') as wf:
    wf.writelines(line_list)
