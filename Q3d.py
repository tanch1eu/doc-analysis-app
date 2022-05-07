# Question 3d.
# BM25 calculation

import string
from stemming.porter2 import stem
import math

# This function returns dictionary collections (index{} and list_docLen{}.
# index{} is a BowDoc collection of term:dictionary of docid:term frequency in the doc.
# list_docLen{} is a collection of docid:docLen for each doc.
def docs_index(input):
    index = {}
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

#This function returns the average document length of the given dataset.
def avgDocLen (dict):
    list = dict.values()
    Sum = sum(list)
    NumDocs = dict.__len__()
    Avg = math.floor(Sum/NumDocs)
    return Avg

def term_at_a_time(I, Q):   # index I is a Dictionary of term:Dictionary of (itemId:freq)
    L={}                    # L is the selected inverted list
    R={}                    # R is a dictionary of docId:relevance
    for list in I.items():
        for id in list[1].items(): # get all document IDs with value 0
            R[id[0]]=0
        if (list[0] in Q):         # select inverted lists based on the query
                L[list[0]]= I[list[0]]
    # print(L)
    for (term, li) in L.items():  # traversal of the selected inverted list
        for (d, f) in li.items(): # for each occurence of doc, update R
                R[d] = R[d]  + f*Q[term]
    # print(R)
    return (L, R)

# This function calculates BM25 score for each document ID (docid) and query (Q).
def BM25_calc(docid, Q):
    N = len(fn)
    k1 = 1.2
    k2 = 100
    b = 0.75
    dL = BowDoc[1][str(docid)]
    K = k1 * ((1 - b) + b * float(dL / AvgDocLen))
    # print("K = " + str(K))
    result1 = term_at_a_time(xn, Q)
    list_L = result1[0]
    BM25 = 0
    for obj in Q.items():
        qf = obj[1]
        n = len(list_L[obj[0]])
        f = 0
        if str(docid) in list_L[obj[0]].keys():
            f = list_L[obj[0]][str(docid)]
        BM = math.log((N + 0.5 - n) / (0.5 + n)) * (((k1 + 1) * f) / (K + f)) * ((k2 + 1) * qf / (k2 + 1))
        # print( qf, n, f)
        # print(BM)
        BM25 += BM
    return BM25

if __name__ == '__main__':

    fn = ["741299newsML.xml", "741309newsML.xml", "780718newsML.xml", "780723newsML.xml", "783802newsML.xml",
          "783803newsML.xml", "807600newsML.xml", "807606newsML.xml", "809481newsML.xml", "809495newsML.xml"]
    stop_words = StopWord()
    BowDoc = docs_index(fn)
    xn = BowDoc[0]       # Collection of term frequencies.
    yn = BowDoc[1]       # Collection of documentID: documentLength
    # print(xn)
    AvgDocLen = avgDocLen(BowDoc[1])

    # Start to parse documents for each query.
    #########################################################################################################

    Query1 = {'british': 1, 'fashion': 1}
    zn = {}
    print("\nAverage document length " + str(AvgDocLen) + " for Query: Bristish fashion >>>")
    for id in yn:
        result = BM25_calc(id, Query1)
        zn[id] = result
        print("Document ID-" + id + ", Length: " + str(yn[id]) + ", BM25 Score= " + str(result))
    z_s = sorted(zn.items(), key=lambda x: x[1],reverse=True)[:3]
    print("\nFor Query: \"British fashion\", three recommended relevant documents and their BM25 scores:")
    for id, val in z_s:
        print("Document ID-" + str(id) + ": " + str(val))
    #########################################################################################################

    Query2 = {'fashion': 1, 'award': 1}
    zn = {}
    print("\nAverage document length " + str(AvgDocLen) + " for Query: fashion award >>>")
    for id in yn:
        result = BM25_calc(id, Query2)
        zn[id] = result
        print("Document ID-" + id + ", Length: " + str(yn[id]) + ", BM25 Score= " + str(result))
    z_s = sorted(zn.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\nFor Query: \"fashion award\", three recommended relevant documents and their BM25 scores:")
    for id, val in z_s:
        print("Document ID-" + str(id) + ": " + str(val))
    #########################################################################################################

    Query3 = {'stock': 1, 'market': 1}
    zn = {}
    print("\nAverage document length " + str(AvgDocLen) + " for Query: stock market >>>")
    for id in yn:
        result = BM25_calc(id, Query3)
        zn[id] = result
        print("Document ID-" + id + ", Length: " + str(yn[id]) + ", BM25 Score= " + str(result))
    z_s = sorted(zn.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\nFor Query: \"stock market\", three recommended relevant documents and their BM25 scores:")
    for id, val in z_s:
        print("Document ID-" + str(id) + ": " + str(val))
    #########################################################################################################

    Query4 = {'british': 1, 'fashion': 1, 'award': 1}
    zn = {}
    print("\nAverage document length " + str(AvgDocLen) + " for Query: british fashion award >>>")
    for id in yn:
        result = BM25_calc(id, Query4)
        zn[id] = result
        print("Document ID-" + id + ", Length: " + str(yn[id]) + ", BM25 Score= " + str(result))
    z_s = sorted(zn.items(), key=lambda x: x[1], reverse=True)[:3]
    print("\nFor Query: \"british fashion award\", three recommended relevant documents and their BM25 scores:")
    for id, val in z_s:
        print("Document ID-" + str(id) + ": " + str(val))