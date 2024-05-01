import os

class KnapsackInstance:
    '''
    >>> filepath = os.path.join('test_instances', 'toy-instance')
    >>> kp = KnapsackInstance.load_from_file(filepath)
    >>> kp
    KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    
    '''
    @staticmethod
    def load_from_file(filepath: str) -> 'KnapsackInstance':
        '''
        '''
        W: list[int] = []
        V: list[int] = []
        C: int = 0
        
        # add code here to load instances
        with open(filepath) as f:
            C = int(f.readline().split(" ")[1])
            for l in f:
                w, v = [int(x) for x in l.split(" ")]
                W.append(w)
                V.append(v)
        
        return KnapsackInstance(W, V, C)

    def __init__(self, W: list[int], V: list[int], C: int) -> None:
        self.W: list[int] = W
        self.V: list[int] = V
        self.C: int = C
        self.size: int = len(W)

    def __repr__(self):
        return f"{__class__.__name__}(W={self.W}, V={self.V}, C={self.C})"

class KnapsackSolver:
    """
    General abstract solver for 01-Knapsack problem

    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)

    >>> s = KnapsackSolver(kp)
    >>> s.weight(X=[1, 1, 1, 1, 1, 1])
    84
    """

    def __init__(self, instance) -> None:
        self._inst = instance
        # 0-1 decision variables
        self._X: list[int] = [0] * self._inst.size

    def solve(self) -> tuple[int, ...]:
        """
        Solves the loaded instance and returns the assignment to the decision
        variables
        """
        raise NotImplementedError

    def weight(self, X: tuple[int, ...]) -> int:
        """
        Computes the total volume of the objects contained in the solution X
        """
        return sum(w * x for w, x in zip(self._inst.W, X))

    def value(self, X: tuple[int, ...]) -> int:
        """
        Computes the total value of the objects contained in the solution X
        """
        return sum(v * x for v, x in zip(self._inst.V, X))


try:
    import doctest
    doctest.testmod()
except:
    print("Unable to load doctests")    