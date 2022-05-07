# PART II
# Question 2, model training set generation using <desc> as Query.

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
    df_ = df.calc_df(coll_)
    bm25_1 = bm25(coll_, "What is being done to counter economic espionage internationally?", df_)
    print('Done.')
    os.chdir('..')
    wFile = open('Model_R101.dat', 'w')
    for (k, v) in sorted(bm25_1.items(), key=lambda x: x[1], reverse=True):
        wFile.write(k + ' ' + str(v) + '\n')
    wFile.close()

    # Create training benchmark for each topic
    writeFile = open('NewTraining_benchmark101.txt', 'w')

    datFile = open('Model_R101.dat')
    file_ = datFile.readlines()
    for line in file_:
        line = line.strip()
        lineStr = line.split()
        if ((float(lineStr[1]) > 1.0) or (float(lineStr[1]) < -8.0)):
            writeFile.write('R101 ' + lineStr[0] + ' 1' + '\n')
        else:
            writeFile.write('R101 ' + lineStr[0] + ' 0' + '\n')
    writeFile.close()
    datFile.close()
