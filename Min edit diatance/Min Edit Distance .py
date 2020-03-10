match = 1
mismatch = 2
insertion  = 1
deletion = 1
gap = 1

matrix = []
s = []

#makeMatrix()

# Create dictionary
costList = []
f = open('costs.csv')
allLines  = f.readlines()
for l in range(len(allLines)):
    allLines[l] = allLines[l].strip('\n')
    cost = [ x for x in allLines[l].split(",")]  #list of list containing costs.csv
    costList.append(cost)
print(costList)

costList2 = []
f = open('costs2.csv')
allLines  = f.readlines()
for l in range(len(allLines)):
    allLines[l] = allLines[l].strip('\n')
    cost2 = [ x for x in allLines[l].split(",")]  #list of list containing costs.csv
    costList2.append(cost2)
print(costList2)

for costs in costList2:


wordList = []
f = open('words.txt')
allLines  = f.readlines()
for l in range(len(allLines)):
    allLines[l] = allLines[l].strip('\n')
    word = [ x for x in allLines[l].split(" ")]  #list of list containing word
    wordList.append(word)
#print(wordList[0])

#Calling all the function for each word

length = len(wordList)
for i in range (0, length):
    for j in range(0, len(wordList[i])-1 ):
        columns = len(wordList[i][0]) + 1
        # print (wordList[i][0])
        rows = len(wordList[i][j+1]) + 1
        # print(wordList[i][j+1])
        sequence1 = wordList[i][0]
        sequence2 = wordList[i][j+1]
        matrix = []
        s = []


'''
1. Why you believe the results are as output by your code.
Answer: According to something In this program we are predicting the next item in such a sequence in the form of a (n − 1)–order
 It predict the probability of the occurrence of word in the test corpus.  
2. The test sentences are extracted randomly from the news stories used in the training data. A sentence is in
either the training data or the test data, but not both. Discuss the pros and cons of this approach.
3. What, in your opinion, is a better way to split the data into training and test components? Give reasons for
your answer. 

'''