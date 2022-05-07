# Question 3a.
# Print out a list of docID:docLen,
# and average document length for the given document collection.

import string
from stemming.porter2 import stem
import math

# This function returns dictionary collections (index{} and list_docLen{}.
# index{} is a BowDoc collection of term:dictionary of docid:term frequency in the doc.
# list_docLen{} is a collection of docid:docLen for each doc.
def docs_index(input):
    index = {}     # initialize the index
    list_docLen = {}
    for file in input:
        start_end = False
        docLen = 0
        for line in open(file):
            line = line.strip()
            if (start_end == False):
                if line.startswith("<newsitem "):
                    for part in line.split():
                        if part.startswith("itemid="):
                            docid = part.split("=")[1].split("\"")[1]
                            break
                if line.startswith("<text>"):
                    start_end = True
            elif line.startswith("</text>"):
                break
            else:
                line = line.replace("<p>", "").replace("</p>", "")
                line = line.translate(str.maketrans('', '', string.digits)).translate(
                    str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
                for term in line.split():
                    docLen += 1
                    term = stem(term.lower())
                    if len(term) > 2 and term not in stop_words:
                        try:
                            try:
                                index[term][docid] += 1
                            except KeyError:
                                index[term][docid] = 1
                        except KeyError:
                            index[term] = {docid: 1}
        list_docLen[docid] = docLen
    return (index, list_docLen)

# This function is used to define a list of stop words that will be used for the whole program.
def StopWord():
    stopwords_f = open('common-english-words.txt', 'r')
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    return stop_words

# This function returns the average document length of the given dataset.
def avgDocLen (dict):
    list = dict.values()
    Sum = sum(list)
    NumDocs = dict.__len__()
    Avg = math.floor(Sum/NumDocs)
    return Avg

if __name__ == '__main__':

    fn = ["741299newsML.xml", "741309newsML.xml", "780718newsML.xml", "780723newsML.xml", "783802newsML.xml",
          "783803newsML.xml", "807600newsML.xml", "807606newsML.xml", "809481newsML.xml", "809495newsML.xml"]
    stop_words = StopWord()
    BowDoc = docs_index(fn)
    xn = BowDoc[0]
    # print(xn)
    print("Average documents length: " + str(avgDocLen(BowDoc[1])))
    for item in BowDoc[1].keys():
        print("Document ID-" + item + " has length: " + str(BowDoc[1][item]) )


