class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n1,m1 = len(img1),len(img1[0])
        n2,m2 = len(img2),len(img2[0])

        img1_d = []
        img2_d = []
        dc = defaultdict(int)
        cnt = 0

        for i in range(n1):
            for j in range(m1):
                if img1[i][j] == 1:
                    img1_d.append((i,j))
        for i in range(n2):
            for j in range(m2):
                if img2[i][j] == 1:
                    img2_d.append((i,j))
        
        
        for r1,c1 in img1_d:
            for r2,c2 in img2_d:
                dc[(r2-r1,c2-c1)] += 1
                cnt = max(cnt,dc[(r2-r1,c2-c1)])

        return cnt
                





