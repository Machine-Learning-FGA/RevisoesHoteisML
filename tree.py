from sklearn import tree
from parser import Parser

P = Parser('AM_RevisoesHoteisCaldas.csv')

X,Y = P.get_data()
x = X[:100]
y = Y[:100]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

result = clf.predict([X[102]])

print (result, Y[102])
