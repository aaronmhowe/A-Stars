### Represents a node within the graph
class Node():
    ## Constructor
    def __init__(self, id, xCoordinate, yCoordinate, altitude, edges):
        self.id = id
        
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.altitude = altitude
        self.edges = edges

    ## Returns whether or not this node is a building
    def isBuilding(self):
        return isinstance(self, BuildingNode)
    
### Represents a BuildingNode within the graph
class BuildingNode(Node):
    ## Constructor
    def __init__(self, id, xCoordinate, yCoordinate, altitude, edges, name, address):
        super().__init__(id, xCoordinate, yCoordinate, altitude, edges)
        self.name = name
        self.address = address
    
    ## Returns whether or not this node is a building
    def isBuilding(self):
        super().isBuilding()

### Represents an edge within the graph
class Edge():
    ## Constructor
    def __init__(self, id, isStair, nodes):
        # TODO: Decide how we'll estimate time of edge
        self.id = id
        
        self.isStair = isStair
        self.nodes = nodes
        self.elevationChange = abs(nodes[0].altitude - nodes[1].altitude)
        
### Represents a route    
class Route():
    ## Constructor
    def __init__(self, startNodeID, endNodeID, avoidStairs=False, avoidSteepTerrain=False):
        ## TODO: This requires A*. We'll pass the startNodeID, endNodeID, and settings
        ## to A* and it'll return a list of nodes, which will be the route's "edges" var
        pass
        # edges = AStar.generateRoutePath(startNodeID, endNodeID, avoidStairs, avoidSteepTerrain)
        
### Represents a route that is specifically saved to a schedule
class ScheduleRoute(Route):
    ## Constructor
    def __init__(self, id, name, startTime, endTime, startNodeID, endNodeID, avoidStairs=False, avoidSteepTerrain=False):
        self.id = id
        
        ## TODO: This requires A*. We'll pass the startNodeID, endNodeID, and settings
        ## to A* and it'll return a list of nodes, which will be the route's "edges" var
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        # edges = AStar.generateRoutePath(startNodeID, endNodeID, avoidStairs, avoidSteepTerrain)
        
### Represents a schedule
class Schedule():
    ## Constructor
    def __init__(self, id, name, scheduleRoutes):
        self.id = id
        self.name = name
        self.scheduleRoutes = scheduleRoutes
        
    ## Adds the given ScheduleRoute to this Schedule's scheduleRoutes
    def addScheduleRoute(self, scheduleRoute):
        self.scheduleRoutes.append(scheduleRoute)