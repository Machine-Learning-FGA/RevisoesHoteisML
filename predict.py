from sklearn import neighbors
from parser import SimpleParser

SP = SimpleParser('AM_RevisoesHoteisCaldas.csv')


def sub_array(array, cols):
    a = []
    cols.sort()
    for i in cols:
        a.append(array[i - 1])
    if len(cols):
        return a
    else:
        return array


X, Y = SP.get_data()
X = [sub_array(sub, [8, 9, 10, 11, 12, 13, 16]) for sub in X]
knn = neighbors.KNeighborsClassifier(n_neighbors=70)
knn.fit(X, Y)

data = input("Tipo "), input("Animadores "), input("Academia "), input("Quadra de tenis "), input("Wifi ")
# knc = knn.predict([data[0]])

data = [data[0] == "Família", data[0] == "Negócios", data[0] == "Sozinho", data[1] == "SIM", data[2] == "SIM", data[3] == "SIM", data[4] == "SIM"]
print(data)
print(knn.predict([data]))
