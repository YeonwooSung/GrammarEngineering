import nltk
from nltk import FeatureChartParser

fcfg = nltk.data.load('P2.fcfg')
parser = FeatureChartParser(fcfg)


def parse_text_to_find_neg_sents(text):
	examples = text.splitlines()
	for sent in examples:
		parses = parser.parse(sent.split())
		numOfTrees = 0
		for tree in parses:
			numOfTrees += 1
		if numOfTrees < 1:
			print(sent)

def parse_text(text):
	examples = text.splitlines()
	for sent in examples:
		print(sent)
		parses = parser.parse(sent.split())
		numOfTrees = 0
		for tree in parses:
			print(tree)

def parse_file(name, mode=1):
	f = open(name, 'r')
	text = f.read()
	f.close()

	if mode == 1:
		parse_text(text)
	else:
		parse_text_to_find_neg_sents(text)


print("================ Positive examples ================")
parse_file('P2.pos', 2)
print("================ Negative examples ================")
parse_file('P2.neg')
