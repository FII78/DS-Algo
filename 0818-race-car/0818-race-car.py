from collections import deque
class Solution:
    """
    initially: step = 0, position = 0 and speed = 1
    Initialize a deque that holds step, position, and speed
    Do BFS on deque by reversing when only necessary
    
    We can check if dest has been reached...that means position = target
    Moving forward: step+1, position+speed, speed*2
    Reversing in 2 cases: 1. if speed is +ve and it passes the target 
                          2. if speed is -ve and speed == 1 but target != position
    
    """
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)]) #step, pos, speed

        while queue:
            steps, pos, speed = queue.popleft()
            
            if pos == target:
                return steps
            
            queue.append((steps+1, pos+speed, speed*2))
            
            currPos = pos + speed
            
            if currPos > target and speed > 0:
                queue.append((steps+1, pos, -1))
                
            if currPos < target and speed < 0:
                queue.append((steps+1, pos, 1))
            
            
        