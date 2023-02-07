class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr_pos = (0, 0)
        prevDir = 'N'
        
        for i in range(len(instructions)):
            currDir = instructions[i]  
            x, y = curr_pos
            
            if currDir == 'G':
                if prevDir == 'N':
                    y += 1
                elif prevDir == 'S':
                    y -= 1
                elif prevDir == 'E':
                    x += 1
                elif prevDir == 'W':
                    x -= 1
                curr_pos = (x, y)
                    
            elif currDir == 'L':
                if prevDir == 'N':
                    prevDir = 'W'
                elif prevDir == 'S':
                    prevDir = 'E'
                elif prevDir == 'E':
                    prevDir = 'N'
                elif prevDir == 'W':
                    prevDir = 'S'
                    
            elif currDir == 'R':
                if prevDir == 'N':
                    prevDir = 'E'
                elif prevDir == 'S':
                    prevDir = 'W'
                elif prevDir == 'E':
                    prevDir = 'S'
                elif prevDir == 'W':
                    prevDir = 'N'
                           
        return True if prevDir != 'N' or curr_pos == (0, 0) else False  
      
                    
        