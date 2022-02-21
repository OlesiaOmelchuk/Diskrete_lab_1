import numpy as np
from sklearn.datasets import load_iris


class Node:

    def __init__(self, X, y, gini):
        self.X = X
        self.y = y
        self.gini = gini
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None


class MyDecisionTreeClassifier:

    def __init__(self, max_depth):
        self.max_depth = max_depth

    def gini(self, left_node: list, right_node: list):
        '''
        A Gini score gives an idea of how good a split is by how mixed the
        classes are in the two groups created by the split.

        A perfect separation results in a Gini score of 0,
        whereas the worst case split that results in 50/50
        classes in each group result in a Gini score of 0.5
        (for a 2 class problem).
        '''
        num_of_left = len(left_node)
        num_of_right = len(right_node)
        num_of_all = num_of_left + num_of_right

        if num_of_left == 0 or num_of_right == 0:
            return 1000

        gini_left = 1
        gini_right = 1
        for feature in range(4):
            probability_left = (left_node.count(feature)/num_of_left)**2
            probability_right = (right_node.count(feature)/num_of_right)**2
            gini_left -= probability_left
            gini_right -= probability_right
        total_gini = (num_of_left*gini_left)/num_of_all + \
            (num_of_right*gini_right)/num_of_all
        return total_gini

    def split_data(self, X, y) -> tuple[int, int]:

        # test all the possible splits in O(N^2)
        # return index and threshold value

        for feature in range(4):
            all_samples = X[:, feature]
            all_thresholds = list(set(all_samples))
            for threshold in all_thresholds:
                left_node = []
                right_node = []
                for index_sample in range(len(y)):
                    sample = all_samples[index_sample]
                    if sample <= threshold:
                        left_node.append(y[index_sample])
                    else:
                        right_node.append(y[index_sample])

    def build_tree(self, X, y, depth=0):

        # create a root node

        # recursively split until max depth is not exeeced

        pass

    def fit(sefl, X, y):

        # basically wrapper for build tree

        pass

    def predict(self, X_test):

        # traverse the tree while there is left node
        # and return the predicted class for it,
        # note that X_test can be not only one example

        pass
