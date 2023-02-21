class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices, reachable =  [], set()
        
        for s,e in edges:
            reachable.add(e)
            
        for v in range(n):
            if v not in reachable:
                vertices.append(v)
                
        return vertices
        
        