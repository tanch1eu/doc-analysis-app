# Question 2a.
# Define a function calc_df to calculate document-frequency (df) for a given BowDoc
# collection and return a term:df dictionary. Call the created method calc_df to display a list of
# term:df pairs for the whole RCV1v2 document collection

import string
from stemming.porter2 import stem

# This function returns a dictionary collection (index),
# in which the 1st element is the terms retrieved from the original xml files,
# and the 2nd element contains the frequency(df) of each term.
def calc_df(input):
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
                            index[term] += 1
                        except KeyError:
                            index[term] = 1
    return index

# This function is used to define a list of stop words that will be used for the whole program.
def StopWord():
    stopwords_f = open('common-english-words.txt', 'r')
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    return stop_words

# This function displays the term:frequency pairs in descending order.
def DisplayCalc_df (list):
    print("There are " + str(len(fn)) + " documents in this dataset and contains " + str(len(list)) + " terms.")
    list_s = sorted(list.items(), key=lambda item: item[1], reverse=True)
    for element in list_s:
        print(element[0] + ": " + str(element[1]))

if __name__ == '__main__':

    fn = ["741299newsML.xml", "741309newsML.xml", "780718newsML.xml", "780723newsML.xml", "783802newsML.xml",
          "783803newsML.xml", "807600newsML.xml", "807606newsML.xml", "809481newsML.xml", "809495newsML.xml"]
    stop_words = StopWord()
    xn = calc_df(fn)
    # print(xn)
    DisplayCalc_df(xn)