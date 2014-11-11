from fuzzywuzzy import process
import codecs

FUZZY_THRESHOLD = 70
MATCHES_COUNT = 3

INPUT_FILE = "test-input.dat"
CORPUS_FILE = "test-corpus.dat"
OUTPUT_FILE = "test-output.dat"

def main():
	# open input file
	input_file = codecs.open(INPUT_FILE, "r", "utf-8")
	# read lines from input file and strip the new line character at the end
	input_list = [x.strip() for x in input_file.readlines()]

	output_file = codecs.open(OUTPUT_FILE, 'w', "utf-8")

	# open input file
	corpus_file = codecs.open(CORPUS_FILE, "r", "utf-8")
	# read lines from input file and strip the new line character at the end
	corpus_list = [x.strip() for x in corpus_file.readlines()]

	for name in input_list:
		# get fuzzy match for name
		matched_list = process.extract(name, corpus_list, limit = MATCHES_COUNT)
		# filter the list of matches to be above the threshold
		filtered_matched_list = filter(lambda t: t[1] >= FUZZY_THRESHOLD, matched_list)

		output_str = '%s' % name + ", " + ", ".join(list(map(lambda t: '(%s, %s)' % (t[0], t[1]), filtered_matched_list))) + "\n"
		output_file.write(output_str)

	output_file.close()

if __name__ == "__main__":
    main()