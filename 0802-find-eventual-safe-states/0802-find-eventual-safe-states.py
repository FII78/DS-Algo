class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        the idea is since the terminal nodes are safe nodes and also the nodes that
        only lead to terminal nodes are safe. We can first re-order the nodes               instead of what goes out I can know from which nodes I can access the current node.
        """
        n = len(graph)
        
        re_order = defaultdict(list)
        out_degree = [0] * n
        
        for i in range(n):
            for nei in graph[i]:
                re_order[nei].append(i)
                out_degree[i] += 1

        queue = deque()
        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)
        
        ret = []
        while queue:
            curr = queue.popleft()
            ret.append(curr)
            #go through the nei of all safe-terminal node and check if 
            #the terminal node was the only node it was connected to 
            for nei in re_order[curr]:
                out_degree[nei] -= 1
                if out_degree[nei] == 0:
                    queue.append(nei)
                    
                
        return sorted(ret)
       