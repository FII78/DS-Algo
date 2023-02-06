class DetectSquares:
    
    """
    Brute force - N**3
    The idea is having one of the point, and then try out every other possiblities. (not effcient)
    
    Geometry:
    Instead of running 3 for loops, we can take from the point and take the diagonal point from the query point given and then verify if it can form a square. y distance == x distance, 
    Supposing the query points are px, py and the diagonal is x,y... check from the hashmap if (x, py) and (px,y)       exist in the hashmap with O(1)...since we can have multiple same points we can multiply them to get all the possiblities.
    

    """

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.pts = []
        
    def add(self, point: List[int]) -> None:
        # increment each time we find point 
        self.pointCount[tuple(point)] += 1
        # maintain a list since we can't change the size of a dictionary 
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        
        for x,y in self.pts:
            # check if their diff is not equal that means we can't have a square and if the query's x and y is equal to the diagonal x and y...meaning the points are not diagonal.
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            # get the point's count from the point dictionary, and multiply the count of each point 
            res += self.pointCount[(x, py)] * self.pointCount[(px, y)]
            
        return res
            
    
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)