from sklearn.neighbors import KNeighborsClassifier

class GenRakel:
    """Genetic algorithm based on the Rakel approach
    GenRakel

    Parameters
    ----------
    k : int, optional, default : 3
        Number of labels in each of the splits
    
    num_iter : int, optional, default : 200
        Number of iterations of our algorithm
    
    base_classif : sklearn classifier, optional, default : MLkNN
        Base classifier for our algorithm

    operator : string, optional, defult : self
        Operator of crossing for evaluating and creating the population
    
    mutator : string, optional, default : self
        Mutator used for mutating the individuals of the population

    metric : string, optional, default : accuracy
        Metric used for seeing the ganancy of an individual of a population

    Attributes
    ----------

    individual : individual of the population with a solution
        Each of the individual will obtain a solution to the problem

    population : array of individuals
        Population created for the problem
     
    """

    def __init__(self, k=3, num_iter=200, base_classif = KNeighborsClassifier(), operator = "self", mutator = "self", metric = "accuracy"):
        """
        Initialize properties and params.

        :param k:
        :param num_iter:
        :param base_classif:
        :param operator:
        :param mutator:
        :param metric:
        """
        self.k = k
        self.num_iter = num_iter
        self.base_classif = base_classif
        self.operator = operator
        self.mutator = mutator
        self.metric = metric

    def fit(self, X, y):
        """
        Trains the model
        
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Train instances.
        
        y : array-like or sparse matrix, shape=(n_samples, n_labels)
            Train labels
        """

    def predict(self, X):
        """
        Predicts using the model
        
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Test instances.
        
        Returns:
        --------
        predictions : array-like, shape=(n_samples, n_labels)
            Label predictions for the test instances. 
    
        """
    
    def predict_proba(self, X):
        """
        Predicts probabilities for each label using the model
        
        Parameters
        ----------
        X : array-like or sparse matrix, shape=(n_samples, n_features)
            Test instances.
        
        Returns:
        --------
        probabilities : array-like, shape=(n_samples, n_labels)
            Label probabilities for the test instances.
        """
    
    def get_params(self):
        """
        Returns the parameters of this model

        Returns:
        --------
        k : int, optional, default : 3
            Number of labels in each of the splits
        
        num_iter : int, optional, default : 200
            Number of iterations of our algorithm
        
        base_classif : sklearn classifier, optional, default : MLkNN
            Base classifier for our algorithm

        operator : string, optional, defult : self
            Operator of crossing for evaluating and creating the population
        
        mutator : string, optional, default : self
            Mutator used for mutating the individuals of the population

        metric : string, optional, default : accuracy
            Metric used for seeing the ganancy of an individual of a population        
        """

        return self.k, self.num_iter, self.base_classif, self.operator, self.mutator, self.metric

    def set_params(self, k=None, num_iter=None, base_classif=None, operator=None, mutator=None, metric=None):
        """
        Set the parameters of our model

        Parameters:
        -----------
        k : int, optional, default : 3
        Number of labels in each of the splits
        
        num_iter : int, optional, default : 200
            Number of iterations of our algorithm
        
        base_classif : sklearn classifier, optional, default : MLkNN
            Base classifier for our algorithm

        operator : string, optional, defult : self
            Operator of crossing for evaluating and creating the population
        
        mutator : string, optional, default : self
            Mutator used for mutating the individuals of the population

        metric : string, optional, default : accuracy
            Metric used for seeing the ganancy of an individual of a population
        """
        if k is not None:
            self.k = k
        if num_iter is not None:
            self.num_iter = num_iter
        if base_classif is not None:
            self.base_classif = base_classif
        if operator is not None:
            self.operator = operator
        if mutator is not None:
            self.mutator = mutator
        if metric is not None:
            self.metric = metric