class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            hor = image[i]
            hor = hor[::-1]
            
            for j in range(len(hor)):
                if hor[j]:
                    hor[j] = 0
                else:
                    hor[j] = 1
            image[i] = hor
            
        return image
            
                
                
            
                
        