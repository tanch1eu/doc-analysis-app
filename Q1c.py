# Question 1c
# Parsing and tokenizing.
# Sort and display document term:freq list by frequency.

import string
from stemming.porter2 import stem

# This class uses Bag-of-Words to represent a document
class BowDoc:
    def __init__(self, Bag_of_words, next=None):
        self.Bag_of_words = Bag_of_words
        self.next = next

# Tokenizing – fill term:freq dictionary for each document.
# The function addTerms() adds new term or increase term frequency when the term occur again.
# This function returns a tuple, in which the 1st element is the number of words in <text> from the original xml files,
# and the 2nd element is a dictionary collection that contains pairs of document id (id) and term_frequency pairs.
def addTerms(file):
    myfile = open(file)
    doc = {}
    word_count = 0
    start_end = False
    file_ = myfile.readlines()
    for line in file_:
        line = line.strip()
        if (start_end == False):
            if line.startswith("<newsitem "):
                for part in line.split():
                    if part.startswith("itemid="):
                        id = part.split("=")[1].split("\"")[1]
                        break
            if line.startswith("<text>"):
                start_end = True
        elif line.startswith("</text>"):
            break
        else:
            line = line.replace("<p>", "").replace("</p>", "")
            line = line.translate(str.maketrans('', '', string.digits)).translate(
                str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
            line = line.replace("\\s+", " ")
            for term in line.split():
                word_count += 1
                term = stem(term.lower())
                if len(term) > 2 and term not in stop_words:
                    try:
                        doc[term] += 1
                    except KeyError:
                        doc[term] = 1
    myfile.close()
    dn = BowDoc((id, doc), None)
    return (dn, word_count)

# This function is used to define a list of stop words that will be used for the whole program.
def StopWord():
    stopwords_f = open('common-english-words.txt', 'r')
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    return stop_words

# This function displays document term:freq list by frequency.
def displayDocInfo(docID, list):
    print("\nSearching result...")
    if docID == 741299:
        print('Document ID-' + list[0].Bag_of_words[0] + ' contains ' + str(len(list[0].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[0]) + ' words.----')
        doc = list[0].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item:item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 741309:
        print('Document ID-' + list[1].Bag_of_words[0] + ' contains ' + str(len(list[1].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[1]) + ' words.----')
        doc = list[1].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 780718:
        print('Document ID-' + list[2].Bag_of_words[0] + ' contains ' + str(len(list[2].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[2]) + ' words.----')
        doc = list[2].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 780723:
        print('Document ID-' + list[3].Bag_of_words[0] + ' contains ' + str(len(list[3].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[3]) + ' words.----')
        doc = list[3].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 783802:
        print('Document ID-' + list[4].Bag_of_words[0] + ' contains ' + str(len(list[4].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[4]) + ' words.----')
        doc = list[4].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 783803:
        print('Document ID-' + list[5].Bag_of_words[0] + ' contains ' + str(len(list[5].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[5]) + ' words.----')
        doc = list[5].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 807600:
        print('Document ID-' + list[6].Bag_of_words[0] + ' contains ' + str(len(list[6].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[6]) + ' words.----')
        doc = list[6].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 807606:
        print('Document ID-' + list[7].Bag_of_words[0] + ' contains ' + str(len(list[7].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[7]) + ' words.----')
        doc = list[7].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 809481:
        print('Document ID-' + list[8].Bag_of_words[0] + ' contains ' + str(len(list[8].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[8]) + ' words.----')
        doc = list[8].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    elif docID == 809495:
        print('Document ID-' + list[9].Bag_of_words[0] + ' contains ' + str(len(list[9].Bag_of_words[1]))
              + ' terms (stems) and '+ str(list_wordcount[9]) + ' words.----')
        doc = list[9].Bag_of_words[1]
        doc_sorted = {k: v for k, v in sorted(doc.items(), key=lambda item: item[1], reverse=True)}
        for stem, freq in doc_sorted.items():
            print(stem + ': ' + str(freq))
    else:
        print("Not Found. Document ID may not in List. Try again.")

# This function generates 2 collections of BowDoc.
# 1st - list - contains BowDoc object term:freq.
# 2nd - list_id - contains BowDoc object DocumentID.
# 3rd - list_wordcount - contains the numbers of wordcount for each document.
def ListCreate(fn):
    for element in fn:
        xn = addTerms(element)
        id = xn[0].Bag_of_words[0]
        yn = xn[0]
        zn = xn[1]
        list.append(yn)
        list_id.append(id)
        list_wordcount.append(zn)

# This function prints out all document IDs.
def printAllDocID():
    print("All Document IDs: ")
    for item in list_id:
        print(item, end=" >>> ")

if __name__ == '__main__':

    fn = ["741299newsML.xml", "741309newsML.xml", "780718newsML.xml", "780723newsML.xml", "783802newsML.xml",
          "783803newsML.xml", "807600newsML.xml", "807606newsML.xml", "809481newsML.xml", "809495newsML.xml"]
    stop_words = StopWord()

    list = []
    list_id = []
    list_wordcount = []
    ListCreate(fn)
    printAllDocID()
    # Sort and display term:freq list for a document.
    val = input("\nEnter a document ID to search:")
    displayDocInfo(int(val), list)