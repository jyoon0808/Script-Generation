import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', "--input", default='_2_dictionary_in_diphone.txt', required=False, type=str,
					help='input file')

parser.add_argument('-o1', '--output1', default='_3_dictionary_frequency.txt', required=False, type=str,
					help='output file name')

parser.add_argument('-o2', '--output2', default='_3_dictionary_mosttoleast.txt', required=False, type=str,
					help='output file name')

args = parser.parse_args()

# Initializing Dictionary
d = {}
word_freq = []
word_list = []
words_only = []

with open(args.input, 'r', encoding='utf-8') as rf:
	for line in rf.readlines():
		text = line.split()
		word_list.extend(line.split())

for word in word_list:
	d[word] = d.get(word, 0) + 1  # initialize word

for key, value in d.items():
	word_freq.append((value, key))
word_freq.sort(reverse=True)

word_freq = list(word_freq)
print(word_freq)

for pair in word_freq:
	words_only.append(pair[1])

with open(args.output1, 'w', encoding='utf-8') as wf:
	for pair in word_freq:
		wf.writelines(str(pair) + "\n")

with open(args.output2, 'w', encoding='utf-8') as wf:
	for word in words_only:
		wf.writelines(str(word) + "\n")
