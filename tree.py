from sklearn import tree
from parser import Parser

P = Parser('AM_RevisoesHoteisCaldas.csv')

X, Y = P.get_data()
x = X[:502]
y = Y[:502]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)

result = clf.predict([X[503]])

print (result, Y[503])
