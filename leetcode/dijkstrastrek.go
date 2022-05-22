package main

import (
	"fmt"
	"math"
)

type Node struct {
	x_coord  int
	y_coord  int
	distance int
	prev     *Node
}

func findLeastDistantNode(priorityQueue *[]*Node) *Node {
	var leastDistantNode *Node
	for _, n := range *priorityQueue {
		if leastDistantNode != nil {
			if n.distance < leastDistantNode.distance {
				leastDistantNode = n
			}
		} else {
			leastDistantNode = n
		}
	}
	return leastDistantNode
}

func findNodeSiblings(distanceMap *map[[2]*Node]int, node *Node) []*Node {
	siblings := []*Node{}
	for coords, _ := range *distanceMap {
		if coords[0] == node {
			siblings = append(siblings, coords[1])
		} else if coords[1] == node {
			siblings = append(siblings, coords[0])
		}
	}
	return siblings
}

func findDistanceBetweenNodes(distanceMap *map[[2]*Node]int, nodeA *Node, nodeB *Node) int {
	for coords, distance := range *distanceMap {
		if coords[0] == nodeA && coords[1] == nodeB {
			return distance
		} else if coords[0] == nodeB && coords[1] == nodeA {
			return distance
		}

	}
	return 0
}

func removeNodeFromQueue(queue *[]*Node, node *Node) {
	newQueue := []*Node{}
	for _, n := range *queue {
		if n.x_coord == node.x_coord && n.y_coord == node.y_coord {
			continue
		}
		newQueue = append(newQueue, n)
	}
	fmt.Println("here", newQueue)
	*queue = newQueue
}

func traverseAllNodes(distanceMap *map[[2]*Node]int, startNode *Node, endNode *Node) {
	// traversed: array - each node has node_name(distance, previous)
	traversed := []*Node{}

	// priority_queue: array - each node has node_name(distance, previous)
	priorityQueue := []*Node{startNode}

	// while priority_queue
	for len(priorityQueue) != 0 {
		// Pick node of priority queue with the least distance
		toTraverse := findLeastDistantNode(&priorityQueue)
		// fmt.Println(findNodeSiblings(distanceMap, toTraverse))
		// Find all the siblings of that node, range over all of it
		for _, siblingNode := range findNodeSiblings(distanceMap, toTraverse) {
			// If the node_distance + distance < sibling_distance
			if findDistanceBetweenNodes(distanceMap, toTraverse, siblingNode)+toTraverse.distance < siblingNode.distance {
				// Update the sibling's value
				// if sibling in traversed, update the siblings value in traversed
				siblingNode.distance = findDistanceBetweenNodes(distanceMap, toTraverse, siblingNode) + toTraverse.distance
				siblingNode.prev = toTraverse
			}
			// if sibling not in traversed, update it to priority_queue
			if !isNodeInList(&traversed, siblingNode) && !isNodeInList(&priorityQueue, siblingNode) {
				priorityQueue = append(priorityQueue, siblingNode)
			}
		}

		// pop the node:toTraverse from priority_queue, add it to traversed
		removeNodeFromQueue(&priorityQueue, toTraverse)
		traversed = append(traversed, toTraverse)
		fmt.Println("PQ is as :", priorityQueue)

	}

	fmt.Println(endNode.x_coord, endNode.y_coord)
	stop := false
	next := endNode.prev
	for !stop {
		if next == startNode {
			stop = true
		}
		fmt.Println(next.x_coord, next.y_coord)
		next = next.prev
	}

}

func isNodeInList(queue *[]*Node, node *Node) bool {
	for _, n := range *queue {
		if n == node {
			return true
		}
	}
	return false
}

// func minimumEffortPath(heights [][]int) int {// }

func main() {
	node00 := &Node{0, 0, 0, nil}
	node01 := &Node{0, 1, math.MaxInt32, nil}
	node02 := &Node{0, 2, math.MaxInt32, nil}
	node10 := &Node{1, 0, math.MaxInt32, nil}
	node11 := &Node{1, 1, math.MaxInt32, nil}
	node12 := &Node{1, 2, math.MaxInt32, nil}
	node20 := &Node{2, 0, math.MaxInt32, nil}
	node21 := &Node{2, 1, math.MaxInt32, nil}
	node22 := &Node{2, 2, math.MaxInt32, nil}

	/*
		00 01 02
		10 11 12
		20 21 22

		00 -2- 01 -5- 02
		3      1	  6
		10 -1- 11 -4- 12
		7	   1	  2
		20 -3- 21 -5- 22

	*/
	// map of distance between each point
	distanceMap := map[[2]*Node]int{
		[2]*Node{node00, node01}: 2,
		[2]*Node{node00, node10}: 3,

		[2]*Node{node01, node02}: 5,
		[2]*Node{node01, node11}: 1,

		[2]*Node{node02, node12}: 6,

		[2]*Node{node10, node11}: 1,
		[2]*Node{node10, node20}: 7,

		[2]*Node{node11, node12}: 4,
		[2]*Node{node11, node21}: 1,

		[2]*Node{node12, node22}: 2,

		[2]*Node{node20, node21}: 3,
		[2]*Node{node21, node22}: 5,
	}

	traverseAllNodes(&distanceMap, node00, node22)
}
