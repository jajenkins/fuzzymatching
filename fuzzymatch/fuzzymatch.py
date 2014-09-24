from fuzzywuzzy import process

FUZZY_THRESHOLD = 90
MATCHES_COUNT = 3

INPUT_FILE = "test-input.dat"
CORPUS_FILE = "test-corpus.dat"

def main():
	# open input file
	input_file = open(INPUT_FILE)
	# read lines from input file and strip the new line character at the end
	input_list = [x.strip() for x in input_file.readlines()]

	# open input file
	corpus_file = open(CORPUS_FILE)
	# read lines from input file and strip the new line character at the end
	corpus_list = [x.strip() for x in corpus_file.readlines()]

	for name in input_list:
		# get fuzzy match for name
		matched_list = process.extract(name, corpus_list, limit = MATCHES_COUNT)
		# filter the list of matches to be above the threshold
		filtered_matched_list = filter(lambda t: t[1] >= FUZZY_THRESHOLD, matched_list)
		print filtered_matched_list


if __name__ == "__main__":
    main()