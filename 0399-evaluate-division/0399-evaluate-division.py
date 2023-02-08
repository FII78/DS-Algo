class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        for each string we can save its relation with other whether if it's deno/numerator
        [["a","b"],["b","c"]], values = [2.0,3.0]
        
        for a: a/b = 2.0
            b: a/b = 2.0 = a:1/2 and b/c: 3.0 = c
            c: b/c = 3.0 = b:1/3
        
        """
        graph = defaultdict(lambda: defaultdict())
        for (A, B), v in zip(equations, values):
            graph[A][B] = v
            graph[B][A] = 1/v
        
        
        for key in graph:
            for i in graph:
                for j in graph:
                    if key in graph[i] and j in graph[key]:
                        graph[i][j] = graph[i][key] * graph[key][j]
        opt = []
        for A,B in queries:
            if B in graph[A]:
                opt.append(graph[A][B])
            else:
                opt.append(-1.00000)
        return opt
  