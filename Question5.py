# PART II
# Question 5
# Implementing IF model with features selection.

import math
from stemming.porter2 import stem

def avg_doc_len(coll):
    tot_dl = 0
    for id, doc in coll.get_docs().items():
        tot_dl = tot_dl + doc.get_doc_len()
    return tot_dl / coll.get_num_docs()

def bm25(coll, q, df):
    bm25s = {}
    avg_dl = avg_doc_len(coll)
    no_docs = coll.get_num_docs()
    for id, doc in coll.get_docs().items():
        query_terms = q.split()
        qfs = {}
        for t in query_terms:
            term = stem(t.lower())
            if len(term) > 2 and term not in stop_words:
                try:
                    qfs[term] += 1
                except KeyError:
                    qfs[term] = 1
        k = 1.2 * ((1 - 0.75) + 0.75 * (doc.get_doc_len() / float(avg_dl)))
        bm25_ = 0.0
        for qt in qfs.keys():
            n = 0
            if qt in df.keys():
                n = df[qt]
                f = doc.get_term_count(qt)
                qf = qfs[qt]
                bm = math.log(1.0 / ((n + 0.5) / (no_docs - n + 0.5)), 2) * (((1.2 + 1) * f) / (k + f)) * (
                            ((100 + 1) * qf) / float(100 + qf))
                bm25_ += bm
        bm25s[doc.get_docid()] = bm25_
    return bm25s

def w4(coll, ben, theta):
    T = {}
    # select T from positive documents and r(tk)
    for id, doc in coll.get_docs().items():
        if ben[id] > 0:
            for term, freq in doc.terms.items():
                try:
                    T[term] += 1
                except KeyError:
                    T[term] = 1
    # calculate n(tk)
    ntk = {}
    for id, doc in coll.get_docs().items():
        for term in doc.get_term_list():
            try:
                ntk[term] += 1
            except KeyError:
                ntk[term] = 1

    # calculate N and R

    No_docs = coll.get_num_docs()
    R = 0
    for id, fre in ben.items():
        if ben[id] > 0:
            R += 1

    for id, rtk in T.items():
        T[id] = ((rtk + 0.5) / (R - rtk + 0.5)) / ((ntk[id] - rtk + 0.5) / (No_docs - ntk[id] - R + rtk + 0.5))

    # calculate the mean of w4 weights.
    meanW4 = 0
    for id, rtk in T.items():
        meanW4 += rtk
    meanW4 = meanW4 / len(T)

    # Features selection
    Features = {t: r for t, r in T.items() if r > meanW4 + theta}
    return Features

def BM25Testing(coll, features):
    ranks = {}
    for id, doc in coll.get_docs().items():
        Rank = 0
        for term in features.keys():
            if term in doc.get_term_list():
                try:
                    ranks[id] += features[term]
                except KeyError:
                    ranks[id] = features[term]
    return ranks

if __name__ == "__main__":

    import sys
    import os
    import coll
    import df

    if len(sys.argv) != 2:
        sys.stderr.write("USAGE: %s <coll-file>\n" % sys.argv[0])
        sys.exit()
    coll_fname = sys.argv[1]

    # PYTHON NOTE: it would be more elegant to create a class that
    # represents the index, and which stores the DF dictionary and other
    # statistics
    stopwords_f = open('common-english-words.txt', 'r')
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    coll_ = coll.parse_rcv_coll(coll_fname, stop_words)

    # Ranking documents with IF Model
    # get features
    os.chdir('..')
    featureFile = open('Model_w4_R101.dat')
    file_ = featureFile.readlines()
    features = {}
    for line in file_:
        line = line.strip()
        lineList = line.split()
        features[lineList[0]] = float(lineList[1])
    featureFile.close()

    # obtain ranks for all documents
    ranks = BM25Testing(coll_, features)
    wFile = open('IF_Result1.dat', 'w')
    for (d, v) in sorted(ranks.items(), key=lambda x: x[1], reverse=True):
        wFile.write(d + ' ' + str(v) + '\n')
    wFile.close()