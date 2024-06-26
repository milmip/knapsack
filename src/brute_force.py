# Exercice https://courses.21-learning.com/runestone/books/published/oci-2224-donc/classic-problems/01-knapsack-short.html#force-brute

from knapsack import KnapsackInstance, KnapsackSolver

class BruteforceKnapsackSolver(KnapsackSolver):
    """
    >>> kp = KnapsackInstance(W=[13, 13, 13, 10, 24, 11], V=[2600, 2600, 2600, 500, 4500, 960], C=50)
    >>> bfs = BruteforceKnapsackSolver(kp)
    >>> Xopt = bfs.solve()
    >>> Xopt in [(0, 1, 1, 0, 1, 0), (1, 0, 1, 0, 1, 0), (1, 1, 0, 0, 1, 0)]
    True
    >>> bfs.value(Xopt)
    9700
    >>> bfs.weight(Xopt)
    50
    >>> bfs.weight(Xopt) <= bfs._inst.C
    True

    """
    
    def __init__(self, instance) -> None:
        # TODO: write the constructor by calling the parent class constructor
        super().__init__(instance)

    @staticmethod
    def _all_solutions(n):
        sols = [None] * 2**n
        
        for i in range(2**n):
            bits = bin(i)[2:]
            k = n - len(bits)
            bits = k * "0" + bits
            sols[i] = tuple([int(b) for b in bits])
        
        return sols
    
    def solve(self) -> tuple[int, ...]:
        # solve by brute force
        solutions = BruteforceKnapsackSolver._all_solutions(self._inst.size)
        
        max = 0
        solMax = None
        for sol in solutions:
            if self.weight(sol) <= self._inst.C:
                val = self.value(sol)
                if val > max:
                    max = val
                    solMax = sol
        
        
        return solMax
    
try:
    import doctest
    doctest.testmod()
except:
    print("Unable to load doctests")    