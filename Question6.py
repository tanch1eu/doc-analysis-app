# Question 6
# Testing IF model
# Calculating top10 precision, recall and F1, and the average precision
# for both IF model and baseline model by the given relevant judgements

def getinfo_fromfile():
    A = {}
    B= {}
    count = 0
    topic = 101
    for line in open("Training101.txt"):
        line = line.strip()
        line1 = line.split()
        A[line1[1]] = int(line1[2])
    for line in open("IF_Result1.dat"):
        line = line.strip()
        line1 = line.split()
        if (count < 10): # top10
            B[line1[0]] = 1
            count += 1
    return (A,B, topic)

if __name__ == "__main__":
    (rel_doc, retrieved_doc, topic) = getinfo_fromfile()
    R = 0
    for (x, y) in rel_doc.items():
        if (y == 1):
            R = R + 1
    print("the number of relevant docs: " + str(R))

    R1 = 0
    for (x, y) in retrieved_doc.items():
        if (y == 1):
            R1 = R1 + 1
    print("the number of retrieved docs: " + str(R1))

    RR1 = 0
    for (x, y) in retrieved_doc.items():
        if (y == 1) and (rel_doc[x] == 1):
            RR1 = RR1 + 1
    print("the number of retrieved docs that are relevant: " + str(RR1))
    r = float(RR1) / float(R)
    p = float(RR1) / float(R1)
    if (RR1 != 0):
        F1 = 2 * p * r / (p + r)
    else: F1 = 0.0
    print("recall = " + str(r))
    print("precision = " + str(p))
    print("F-Measure = " + str(F1))

    wFile = open('EResult1.dat', 'a')
    wFile.write(str(topic) + ' ' + str(p) + ' ' + str(r) + ' ' + str(F1) + ' ' + '\n')
    wFile.close()

