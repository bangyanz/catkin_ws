#!/usr/bin/env python

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
	return ((abs(a.x - b.x) + abs(a.y - b.y))*2)

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
	poseStampedList = []
	#path.poses = [PoseStamped()]
	currentIndex = 0
	pathList = []

	print "getting path"
	while not IsSame(currentNode, start):
		#path.poses[currentIndex].pose.position = currentNode
		print currentNode
		pathList.append(currentNode)
		currentNode = parents[currentNode]
		currentIndex += 1

	#path.poses[currentIndex].pose.position = start
	pathList.append(start)

	publishablePath = MakeGridCellsFromList(pathList)
	print "found path"
	pathPublisher.publish(publishablePath)

	return pathList

def MakeGridCellsFromList (cellList):
	gridCells = GridCells()
	gridCells.cell_width = 1
	gridCells.cell_height = 1
	gridCells.cells = cellList
	gridCells.header.frame_id = 'map'
	return gridCells

def HashPoint (point):
	return ("x"+str(point.x)+"y"+str(point.y)+"z"+str(point.z))

def Waypoints (pointList):

	print "waypoints!"

	waypointpub = rospy.Publisher('waypoints', GridCells)
	WaypointCells = []

	i = 0
	current_state = 2

	WaypointCells.append(pointList[0])

	for item in pointList:
		current_point = item
		if (i < len(pointList)-1):
			next_point = pointList[i+1]
			i += 1

			#if the x coordinate is changing and the y coordinate is staying the same
			if ((not(next_point.x - current_point.x == 0)) and (next_point.y - current_point.y == 0)):
				if (current_state == 1):
					WaypointCells.append(current_point)
					publishableWaypoints = MakeGridCellsFromList(WaypointCells)
					waypointpub.publish(publishableWaypoints)
					time.sleep(.2)

				current_state = 0	
				
			#if the x coordinate is staying the same and the y coordinate is changing
			elif ((next_point.x - current_point.x == 0) and (not(next_point.y - current_point.y == 0))):
				if (current_state == 0):
					WaypointCells.append(current_point)
					publishableWaypoints = MakeGridCellsFromList(WaypointCells)
					waypointpub.publish(publishableWaypoints)
					time.sleep(.2)
				current_state = 1


				
			else:
				print "something is broken"
				print current_point
				print next_point

	WaypointCells.append(pointList[len(pointList)-1])

	publishableWaypoints = MakeGridCellsFromList(WaypointCells)
	waypointpub.publish(publishableWaypoints)
	time.sleep(.5)

	print WaypointCells

	return WaypointCells
	

def SearchForGoal (gridMap, start, goal):
	print "starting a thing"
	
	#Lots of data things
	parents = {}
	parents[start] = None
	costs = {}
	costs[HashPoint(start)] = 0
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
		
		#get from frontier and update lists
		p, currentNode = frontier.get()
		if currentNode not in visited:
			print currentNode
			frontierList.remove(currentNode)
			visited.append(currentNode)

			#publishing
			publishableFrontier = MakeGridCellsFromList(frontierList)
			frontierPublisher.publish(publishableFrontier)
			publishableVisited = MakeGridCellsFromList(visited)
			visitedPublisher.publish(publishableVisited)

			#if found goal
			if (IsSame(currentNode, goal)):
				success = 1
				break

			for neighbor in GetNeighbors(currentNode, gridMap):
				costToNeighbor = costs[HashPoint(currentNode)] + 1
			
				if neighbor not in found or costs[HashPoint(neighbor)] > costToNeighbor:

					costs[HashPoint(neighbor)] = costToNeighbor

					priority = costToNeighbor + GetHeuristic(neighbor, goal)
					frontier.put((priority, neighbor))

					if neighbor not in found:
						frontierList.append(neighbor)
						found.append(neighbor)
					parents[neighbor] = currentNode
	
	if success:
		return parents, costs, currentNode
	else:
		raise NoPathError("There is no path!")


