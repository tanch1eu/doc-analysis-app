# Question 2b.
# Define a function tfidf to calculate tf*idf value of every term in a BowDoc in a given
# BowDoc collection. It calculates a term:tfidf dictionary for each document,
# then returns a dictionary of docID: term:tfidf dictionary.
# Using the defined function to print out top 15 terms (with its value of tf*idf eight) for each document.

import string
from stemming.porter2 import stem
import math

# This function returns a dictionary collection (index),
# in which the 1st element is the terms retrieved from the original xml files,
# and the 2nd element contains the frequency(df) of each term.
def docs_index(input):
    index = {}  # initialize the index
    for file in input:
        start_end = False
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
                    term = stem(term.lower())
                    if len(term) > 2 and term not in stop_words:
                        try:
                            try:
                                index[docid][term] += 1
                            except KeyError:
                                index[docid][term] = 1
                        except KeyError:
                            index[docid] = {term: 1}
    return index

# This function is used to define a list of stop words that will be used for the whole program.
def StopWord():
    stopwords_f = open('common-english-words.txt', 'r')
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    return stop_words

def c_df(docs):
    """Calculate DF of each term in vocab and return as term:df dictionary."""
    df_ = {}
    for id, doc in docs.items():
        for term in doc.keys():
            try:
                df_[term] += 1
            except KeyError:
                df_[term] = 1
    return df_

def c_idf(docs):
    """"Calculate iDF of each term in vocab and return as term:idf dictionary"""
    df = c_df(docs)
    idf_ = {}
    for term, val in df.items():
        df[term] = math.log(len(fn)/float(val))
        idf_[term] = df[term]
    return idf_

def c_tf(d, docs):
    """"Calculate TF of a document and return as term:tf dictionary"""
    tf_ = {}
    for term, val in docs[d].items():
        docs[d][term] = math.log(float(val)) + 1
        tf_[term] = docs[d][term]
    return tf_

def c_tfidf (doctf, idf):
    """"Calculate TF*iDF of each term of a document and return as term:tfidf dictionary"""
    tfidf_ = {}
    for term, val in doctf.items():
        tfidf_[term] = doctf[term]*idf[term]
    return tfidf_

# This function displays the top 15 tf*idf of a document in descending order.
def DisplayCalc_tfidf (d, list):
    tf = c_tf(d, xn)  # Calculate tf of document ID-741299 from dictionary.
    tfidf = c_tfidf(tf, x_idf)
    top15_result = {k: v for k, v in sorted(tfidf.items(), key=lambda item: item[1], reverse=True)[:15]}
    print("\nDocument ID-" + str(d) + " contains " + str(len(list[d])) + " terms.")
    for element in top15_result.items():
        print(element[0] + ": " + str(element[1]))

if __name__ == '__main__':

    fn = ["741299newsML.xml", "741309newsML.xml", "780718newsML.xml", "780723newsML.xml", "783802newsML.xml",
          "783803newsML.xml", "807600newsML.xml", "807606newsML.xml", "809481newsML.xml", "809495newsML.xml"]
    stop_words = StopWord()

    xn = docs_index(fn)
    # print(xn)
    x_idf = c_idf(xn)                   # Calculate idf of total 10 documents.
    # print(x_idf)
    for key in xn.keys():
        DisplayCalc_tfidf(key, xn)     # Calculate tf*idf of each document in the given dataset.
