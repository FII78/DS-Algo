class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        opt = [None] * (len(adjacentPairs) + 1)
        graph = defaultdict(list)
        
        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        
        for key in graph:
            # if the list of pairs is 1 it means it's either the first element or last element
            if len(graph[key]) == 1:
                opt[0] = key
                opt[1] = graph[key][0]
                break
        
        last_idx = 1
        while last_idx < len(adjacentPairs):
            """
            get last value and access it's list of pair values
            start = 1
            last = opt[1] = 2
            last_pairs = graph[2] = [1,3]
            - I want to remove 1 since I've already added it to the opt.
            last_pairs.remove(1) # the prev element from the opt since it's the pair of the last               element.
            - Append the first value from the list of pairs

            """
            last_value = opt[last_idx]
            last_pair = graph[last_value]
            prev = opt[last_idx - 1]
            last_pair.remove(prev)
            next_elem = last_pair[0]
            opt[last_idx + 1] = next_elem
            last_idx += 1            
            
        return opt
           
            
        
        