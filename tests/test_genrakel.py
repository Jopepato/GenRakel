import pytest
import unittest
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from genrakel import __version__
from genrakel.genrakel_ import GenRakel

def test_version():
    assert __version__ == '0.1.0'

class GenRakelTest(unittest.TestCase):
    def test_init(self):
        classifier = GenRakel()

        self.assertNotEqual(classifier, None)
    
    def test_getParams(self):
        classifier = GenRakel()
        k, num_iter, base_classif, operator, mutator, metric = classifier.get_params()
        self.assertEqual(k, 3)
        self.assertEqual(num_iter, 200)
        self.assertEqual(type(base_classif), type(KNeighborsClassifier()))
        self.assertEqual(operator, "self")
        self.assertEqual(mutator, "self")
        self.assertEqual(metric, "accuracy")

    def test_setParamsInit(self):
        classifier = GenRakel(k=5, num_iter=400, base_classif=SVC(), operator = "Something", mutator = "AnotherThing", metric = "recall")
        k, num_iter, base_classif, operator, mutator, metric = classifier.get_params()
        self.assertEqual(k, 5)
        self.assertEqual(num_iter, 400)
        self.assertEqual(type(base_classif), type(SVC()))
        self.assertEqual(operator, "Something")
        self.assertEqual(mutator, "AnotherThing")
        self.assertEqual(metric, "recall")
    
    def test_setParams(self):
        classifier = GenRakel()
        classifier.set_params(k=5, operator="changed", metric="recall")
        k, num_iter, base_classif, operator, mutator, metric = classifier.get_params()
        self.assertEqual(k, 5)
        self.assertEqual(num_iter, 200)
        self.assertEqual(type(base_classif), type(KNeighborsClassifier()))
        self.assertEqual(operator, "changed")
        self.assertEqual(mutator, "self")
        self.assertEqual(metric, "recall")

if __name__ == '__main__':
    unittest.main()