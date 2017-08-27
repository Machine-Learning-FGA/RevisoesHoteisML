from sklearn import tree
from sklearn import neighbors
from parser import Parser, SimpleParser

SP = SimpleParser('AM_RevisoesHoteisCaldas.csv')
P = Parser('AM_RevisoesHoteisCaldas.csv')

interval = 50


def slice(array, a, b):
    return array[a:b]


for parser in [P, SP]:
    A = [0, 0]
    X, Y = parser.get_data()
    for z in range(0, 500, interval):
        x = X[0:z] + X[z + interval:]
        y = Y[0:z] + Y[z + interval:]

        clf = tree.DecisionTreeClassifier()
        knn = neighbors.KNeighborsClassifier(n_neighbors=50)

        clf = clf.fit(x, y)
        knn.fit(x, y)
        a = [0, 0]
        check = slice(X, z, z + interval), slice(Y, z, z + interval)
        for data in zip(check[0], check[1]):
            trc = clf.predict([data[0]])
            knc = knn.predict([data[0]])
            result = "Expected {2}:\n\ttree {0}\n\tknn {1}".format(trc, knc, data[1])

            if trc == data[1]:
                a[0] += 1
            if knc == data[1]:
                a[1] += 1
            # print(result)
        lenght = len(check[0])
        A[0] += a[0] / lenght
        A[1] += a[1] / lenght
        print('The array in range{} len({}) generate the result {}\n\ttree%{}\n\tknn%{}'.format(
            (z, z + interval), lenght, a, a[0] / lenght * 100, a[1] / lenght * 100))
    print(A)
