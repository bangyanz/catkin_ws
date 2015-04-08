import rospy, tf

from nav_msgs.msg import GridCells
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

import time

import Queue

#This is a library that can be called to perform specific AStar functions

#This implementation is based on the A* implementation found at http://www.redblobgames.com/pathfinding/a-star/implementation.html#sec-1-4

#This library will only work if the following values are held by certain variables

#point A
#X coordinate = A.x
#Y coordinate = A.y
#Z coordinare = A.z

#OccupancyGrid gridMap
#data[0] = gridMap.data[0]
#mapmetadata = gridMap.info
#width = gridMap.info.width
#height = gridMap.info.height

class NoPathError(Exception):

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
    

def GetData (x, y, gridMap):
	width = gridMap.info.width
	height = gridMap.info.height
	if (x < 0 or x > width or y < 0 or y > height):
		return 1
	dataLocation = (height * y) + x
	return gridMap.data[dataLocation]

def GetHeuristic (a, b):
	return ((abs(a.x - b.x) + abs(a.y - b.y)) * 2)

def IsSame (a, b):
	return (a.x == b.x and a.y == b.y)

def GetNeighbors (a, gridMap):
	neighbors = []
	#north
	if (GetData(a.x, a.y + 1, gridMap) == 0):
		neighbors.append(Point(a.x, a.y + 1, 0))
	#east
	if (GetData(a.x + 1, a.y, gridMap) == 0):
		neighbors.append(Point(a.x + 1, a.y, 0))
	#south
	if (GetData(a.x, a.y - 1, gridMap) == 0):
		neighbors.append(Point(a.x, a.y - 1, 0))
	#west
	if (GetData(a.x - 1, a.y, gridMap) == 0):
		neighbors.append(Point(a.x - 1, a.y, 0))
	return neighbors


def GetPath (gridMap, start, goal):
	pathPublisher = rospy.Publisher('path', GridCells) 
	#pa = []
	#pa.append(Point(1, 1, 0))
	#blankPath = MakeGridCellsFromList (pa)
	#pathPublisher.publish(blankPath)
	#time.sleep(1)

	parents, costs, currentNode = SearchForGoal(gridMap, start, goal)
	path = Path()
	#poseStampedList = []
	#path.poses = [PoseStamped()]
	currentIndex = 0
	pathList = []

	while not IsSame(currentNode, start):
		#path.poses[currentIndex].pose.position = currentNode
		pathList.append(currentNode)
		currentNode = parents[currentNode]
		currentIndex += 1

	#path.poses[currentIndex].pose.position = start
	pathList.append(start)

	print pathList

	publishablePath = MakeGridCellsFromList(pathList)
	print "found path"
	pathPublisher.publish(publishablePath)

	return path

def MakeGridCellsFromList (cellList):
	gridCells = GridCells()
	gridCells.cell_width = 1
	gridCells.cell_height = 1
	gridCells.cells = cellList
	gridCells.header.frame_id = 'map'
	return gridCells
	

def SearchForGoal (gridMap, start, goal):
	print "starting a thing"
	
	#Lots of data things
	parents = {}
	parents[start] = None
	costs = {}
	costs2 = {}
	costs[start] = 0
	costs2[start] = 0
	frontierList = [start]
	visited = []
	found = [start]

	#The Frontier
	frontier = Queue.PriorityQueue()
	frontier.put((0, start))

	#publishers
	frontierPublisher = rospy.Publisher('frontier', GridCells) 
	visitedPublisher = rospy.Publisher('visited', GridCells) 

	print "I'm so ready"

	success = 0

	while not frontier.empty():
		time.sleep(.03)
		#publishing
		publishableFrontier = MakeGridCellsFromList(frontierList)
		frontierPublisher.publish(publishableFrontier)
		publishableVisited = MakeGridCellsFromList(visited)
		visitedPublisher.publish(publishableVisited)
		
		#get from frontier and update lists
		p, currentNode = frontier.get()
		print currentNode
		frontierList.remove(currentNode)
		visited.append(currentNode)
		print costs2[currentNode]

		#if found goal
		if (IsSame(currentNode, goal)):
			success = 1
			break

		for neighbor in GetNeighbors(currentNode, gridMap):
			costToNeighbor = costs[currentNode] + 1
		
			if neighbor not in found:

				costs[neighbor] = costToNeighbor
				found.append(neighbor)

				priority = costToNeighbor + GetHeuristic(neighbor, goal)
				frontier.put((priority, neighbor))
				costs2[neighbor] = priority

				if neighbor not in frontierList:
					frontierList.append(neighbor)
				parents[neighbor] = currentNode
	
	if success:
		return parents, costs, currentNode
	else:
		raise NoPathError("There is no path!")

def GetPathServer():
	rospy.init_node('GetPathServer')
	service = rospy.Service('GetPath', Pathsrv, GetPath)
	rospy.spin()

if __name__ == "__main__":
	GetPathServer()