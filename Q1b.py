# Question 1b
# Parsing and tokenizing with Stopping words removal and stemming of terms

import string
from stemming.porter2 import stem

# This class uses Bag-of-Words to represent a document
class BowDoc:
    def __init__(self, Bag_of_words, next=None):
        self.Bag_of_words = Bag_of_words
        self.next = next

class Collection_BowDoc:
    def __init__(self, hnode):
        self.head = hnode

    def insert(self, nnode):
        if self.head != None:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = nnode

    def getDocID(self):
        if self.head != None:
            p = self.head
            while p != None:
                print(p.Bag_of_words[0], end=" ")
                if p.next != None:
                    print('>>>', end=" ")
                p = p.next
        else:
            print('Error. Empty list!')


# This function can display all documents ID in the 1st Collection_BowDoc class (list1).
def printAllDocID():
    print("\nAll docs ID: ")
    list1.getDocID()

# This function displays term list with a given docID, by searching the 2nd collection of BowDoc (list2).
def printDocInfo(docID, list):
    print("\nSearching result: ")
    if docID == 741299:
        print('Document ID-' + list[0].Bag_of_words[0] + ' contains ' + str(len(list[0].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[0].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 741309:
        print('Document ID-' + list[1].Bag_of_words[0] + ' contains ' + str(len(list[1].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[1].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 780718:
        print('Document ID-' + list[2].Bag_of_words[0] + ' contains ' + str(len(list[2].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[2].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 780723:
        print('Document ID-' + list[3].Bag_of_words[0] + ' contains ' + str(len(list[3].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[3].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 783802:
        print('Document ID-' + list[4].Bag_of_words[0] + ' contains ' + str(len(list[4].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[4].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 783803:
        print('Document ID-' + list[5].Bag_of_words[0] + ' contains ' + str(len(list[5].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[5].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 807600:
        print('Document ID-' + list[6].Bag_of_words[0] + ' contains ' + str(len(list[6].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[6].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 807606:
        print('Document ID-' + list[7].Bag_of_words[0] + ' contains ' + str(len(list[7].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[7].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 809481:
        print('Document ID-' + list[8].Bag_of_words[0] + ' contains ' + str(len(list[8].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[8].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    elif docID == 809495:
        print('Document ID-' + list[9].Bag_of_words[0] + ' contains ' + str(len(list[9].Bag_of_words[1])) + ' terms.')
        for stem, freq in list[9].Bag_of_words[1].items():
            print(stem + ': ' + str(freq))
    else:
        print("Not Found. Document ID may not in List. Try again.")

# This function generates 2 collections of BowDoc.
# 1st - list1 - is a linked-list
# 2nd - list2 - is an array
def ListCreate (yn):
    for element in yn:                    # add elements (nodes) into list1 and list2.
        xn = addTerms(element)
        list1.insert(xn)
        list2.append(xn)

# Tokenizing – fill term:freq dictionary for each document.
# The function addTerms() adds new term or increase term frequency when the term occur again.
# This function returns a tuple, in which the 1st element is the number of words in <text> from the original xml files,
# and the 2nd element is a dictionary collection that contains pairs of document id (id) and term_frequency pairs.
def addTerms(file):
    myfile = open(file)
    doc = {}
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
                term = stem(term.lower())
                if len(term) > 2 and term not in stop_words:
                    try:
                        doc[term] += 1
                    except KeyError:
                        doc[term] = 1
    myfile.close()
    dn = BowDoc((id, doc), None)
    return (dn)

# This function is used to define a list of stop words that will be used for the whole program.
def StopWord():
    stopwords_f = open('common-english-words.txt', 'r')
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    return stop_words

if __name__ == '__main__':

    fn = ["741309newsML.xml", "780718newsML.xml", "780723newsML.xml", "783802newsML.xml", "783803newsML.xml",
          "807600newsML.xml", "807606newsML.xml", "809481newsML.xml", "809495newsML.xml"]
    stop_words = StopWord()
    x0 = addTerms("741299newsML.xml")
    list1 = Collection_BowDoc(x0)          # initialize first head of the linked-list list1 (1st Collection of BowDoc).
    list2 = []                             # initialize list2 is an empty array (2nd Collection of BowDoc).
    list2.append(x0)
    ListCreate(fn)
    # print out all documents IDs in the list.
    printAllDocID()
    # display term:freq pairs for a given docID, by searching in collection of BowDoc (list2).
    val = input("\nEnter a document ID to search:")
    printDocInfo(int(val), list2)