import numpy as np 
import matplotlib.pyplot as plt


def drawPR():
    r = "0.0153	0.0282	0.0433	0.0602	0.0748	0.09	0.1017	0.1149	0.125	0.1384"
    p = "0.9	0.85	0.867	0.9	0.9	0.9	0.871	0.863	0.833	0.83"

    #SONTUNGMTP
    # r = "0.017	0.017	0.033	0.05	0.05	0.067	0.083	0.083	0.083	0.1"
    # p = "1	0.5	0.67	0.75	0.6	0.67	0.71	0.625	0.56	0.6"
    p = p.split("\t")
    r = r.split("\t")

    p = list(map(float, p))
    r = list(map(float, r))

    graph = plt.plot(r,p, 'r--', r,p, "bs")
    plt.xlabel('Độ đầy đủ')
    plt.ylabel('Độ chính xác')
    plt.title('Đường cong P/R trung bình')
    plt.ylim(0.5,1)
    plt.show()

drawPR()
# ---------------------------

def computePR():
    s = "0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.133	0.15	0.167"

    listR = [
    "0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.133	0.15	0.167", 
    "0.017	0.033	0.05	0.067	0.083	0.083	0.083	0.083	0.1	0.117",
    "0.017	0.017	0.033	0.05	0.05	0.067	0.083	0.083	0.083	0.1", 
    "0.017	0.033	0.05	0.067	0.083	0.1	0.1	0.117	0.133	0.133",
    "0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.133	0.15	0.167", 
    "0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.133	0.133	0.15",
    "0.017	0.017	0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.133", 
    "0	0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.117	0.133",
    "0.017	0.033	0.05	0.067	0.083	0.1	0.1	0.117	0.117	0.117", 
    "0.017	0.033	0.05	0.067	0.083	0.1	0.117	0.133	0.15	0.167"]

    listP = [
    "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	9/9	10/10", 
    "1/1	2/2	3/3	4/4	5/5	5/6	5/7	5/8	6/9	7/10", 
    "1/1	1/2	2/3	3/4	3/5	4/6	5/7	5/8	5/9	6/10",
    "1/1	2/2	3/3	4/4	5/5	6/6	6/7	7/8	8/9	8/10",
    "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	9/9	10/10",
    "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	8/9	9/10", 
    "1/1	1/2	1/3	2/4	3/5	4/6	5/7	6/8	7/9	8/10",
    "0/1	1/2	2/3	3/4	4/5	5/6	6/7	7/8	7/9	8/10", 
    "1/1	2/2	3/3	4/4	5/5	6/6	6/7	7/8	7/9	7/10", 
    "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	9/9	10/10"]

    listFloatR = []
    for r in listR:
        r = r.split("\t")
        r = list(map(float, r))
        listFloatR.append(r)
    RTB = np.array(listFloatR)
    RTB = RTB.sum(axis=0)

    for i, item in enumerate(RTB):
        RTB[i] = item/10
    print("RTB: ", RTB)


    lista = []
    for p in listP:
        p = p.replace("\t", " ")
        p = p.split(" ")
        # print(p)
        pi = []
        for item in p:
            a, b = item.split("/")
            c = float(a) / float(b)
            pi.append(c)
        # p = list(map(float, p))
        # print(r)
        # r = float(r)
        lista.append(pi)
    lista = np.array(lista)
    # print(lista)

    PTB = lista.sum(axis=0)
    print("----")
    for i, item in enumerate(PTB):
        PTB[i] =  float("{0:.3f}".format(item/10))
    print( "PTB:", PTB)

# computePR()
# -------------

def computerecall():
    string = "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	9/9	10/10"
    string = "1/1 2/2 3/3 4/4 5/5 5/6 5/7 5/8 6/9 7/10"
    string = "1/1	1/2	2/3	3/4	3/5	4/6	5/7	5/8	5/9	6/10"
    s = "1/1	2/2	3/3	4/4	5/5	6/6	6/7	7/8	8/9	8/10"
    s= "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	9/9	10/10"
    s = "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	8/9	9/10"
    s = "1/1	1/2	1/3	2/4	3/5	4/6	5/7	6/8	7/9	8/10"
    s = "0/1	1/2	2/3	3/4	4/5	5/6	6/7	7/8	7/9	8/10"
    s = "1/1	2/2	3/3	4/4	5/5	6/6	6/7	7/8	7/9	7/10"
    s = "1/1	2/2	3/3	4/4	5/5	6/6	7/7	8/8	9/9	10/10"

    string = s.replace("\t", " ")
    splitstr = string.split(" ")
    print (splitstr)
    recall = []
    for item in splitstr:
        ri = item.split('/')[0]
        ri = int(ri)/60
        print (ri)
        recall.append(ri)
    print("----")

    for item in recall:
        print("%.3f" % item)
    print (recall)


#-------------------------------------------------____#
def computeMAP():
    liststr = ["(1+1+1+1+1+1+1+1+1+1)/10 = 1.000", "(1/1+2/2+3/3+4/4+5/5+6/9+7/10)/7 = 0.910",
    "(1/1+2/3+3/4+4/6+5/7+6/10)/6 = 0.733","(1/1+2/2+3/3+4/4+5/5+6/6+7/8+8/9)/8 = 0.970",
    "(1+1+1+1+1+1+1+1+1+1)/10 = 1.000","(1+1+1+1+1+1+1+1+9/10)/9 = 0.990",
    "(1/1+2/4+3/5+4/6+5/7+6/8+7/9+8/10)/8 = 0.726","(1/2+2/3+3/4+4/5+5/6+6/7+7/8+8/10)/8 = 0.760",
    "(1/1+2/2+3/3+4/4+5/5+6/6+7/8)/7 = 0.982","(1+1+1+1+1+1+1+1+1+1)/10 = 1.000"]
    sum = 0
    for s in liststr:
        s = s.replace("\t", "")
        s = s.replace(" ", "")
        s = float(s[-5:])
        sum+=s
        print (s)
    print("---")
    print ("map:",sum/10)


#-------------------------------------------------____#
