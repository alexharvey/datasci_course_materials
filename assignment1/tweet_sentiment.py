import csv
import json
import sys
import StringIO

def hw(sent_file, tweet_file):
    with open(sent_file) as csvfile:
        data = list(csv.DictReader(csvfile, fieldnames=['key', 'value'], delimiter='\t'))
        print(data)

    with open(tweet_file) as jsonfile:
        for line in jsonfile:
            tweet = json.loads(line)
            print tweet


def lines(fp):
    print str(len(fp.readlines()))

def main():
    if len(sys.argv) == 2:
        sent_file = open(sys.argv[1])
        tweet_file = open(sys.argv[2])
    else:
        sent_file = '/Users/alex/git/datasci_course_materials/assignment1/AFINN-111.txt'
        tweet_file = '/Users/alex/git/datasci_course_materials/assignment1/output.json'


    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
