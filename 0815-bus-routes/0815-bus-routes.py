class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        initial approach:
            Graph:
            1 -> (2,7) #list of stops I can go 
            2 -> (1,7)
            7 -> (1,2,3,6)
            3 -> (6,7)
            6 -> (3,7)
            
            # for every stop go dfs over every possible stop
            # it wouldn't work (TLE) since the bus route can be 10^5
        
        1 -> route 0 # using the idx as idx
        2 -> route 0
        7 -> route 0, route 1
        3 -> route 1
        6 -> route 1
        # building grap n*500
        
        [[1,2,7],[3,6,7]]
             0      1     route _id
        {1: {0}, 2: {0}, 7: {0, 1}, 3: {1}, 6: {1}}
        
        # stop to route relation # for every stop look for how many routes it belongs to, loop through the stops with visited set in that route
        # record already visited route, we know if a route is already visited we've alredy visited the stops in that route.
        
        Time complexity: for building the graph: m routes n stops ... m*n
                         bfs: looping through all the nodes for the entire 
                              route and stops with worst case m*n
                              O(M*N) - number of routes * number of bus stops
        Space: O(M*N) for the graph
          
        """
        
        graph = defaultdict(set)
        
        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                graph[stop].add(i)
        
        buses = 0
        queue = deque([source])
        
        visited_busStop = set()
        visited_routes = set()
        
        visited_busStop.add(source)
        
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return buses
                
                for route_id in graph[stop]:
                    if route_id not in visited_routes:
                        visited_routes.add(route_id)
                        for bus_stop in routes[route_id]:
                            if bus_stop not in visited_busStop:
                                queue.append(bus_stop)
                                visited_busStop.add(bus_stop)
            buses += 1
                
        return -1
                        
                     
                     
                    
        
        
                
        
       