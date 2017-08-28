import numpy
from parser import Parser, SimpleParser
from pandas import read_csv
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

def univariate_selection():
    # feature extraction
    test = SelectKBest(score_func=chi2, k=4)
    fit = test.fit(X, Y)
    # summarize scores
    numpy.set_printoptions(precision=3)
    print(fit.scores_)
    features = fit.transform(X)
    # summarize selected features
    print(features[0:5,:])

def recursive_feature_elimination():
    model = LogisticRegression()
    rfe = RFE(model, 3)
    fit = rfe.fit(X, Y)
    print("Num Features: ", fit.n_features_)
    print("Selected Features: ", fit.support_)
    print("Feature Ranking: ", fit.ranking_)

def principal_component_analysis():
    # feature extraction
    pca = PCA(n_components=3)
    fit = pca.fit(X)
    # summarize components
    print("Explained Variance: %s") % fit.explained_variance_ratio_
    print(fit.components_)

def feature_importance():
    model = ExtraTreesClassifier()
    model.fit(X, Y)
    print(model.feature_importances_)

X, Y = SimpleParser('AM_RevisoesHoteisCaldas.csv').get_data()

univariate_selection()
# recursive_feature_elimination()
# principal_component_analysis()
# feature_importance()
