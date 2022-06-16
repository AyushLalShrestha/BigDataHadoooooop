package main

import (
	"fmt"
)

func getValidSiblings(node [2]int, lenX int, lenY int) [][2]int {
	validSibling := [][2]int{}
	if 0 <= node[1]+1 && node[1]+1 < lenY {
		validSibling = append(validSibling, [2]int{node[0], node[1] + 1})
	}
	if 0 <= node[1]-1 && node[1]-1 < lenY {
		validSibling = append(validSibling, [2]int{node[0], node[1] - 1})
	}
	if 0 <= node[0]+1 && node[0]+1 < lenX {
		validSibling = append(validSibling, [2]int{node[0] + 1, node[1]})
	}
	if 0 <= node[0]-1 && node[0]-1 < lenX {
		validSibling = append(validSibling, [2]int{node[0] - 1, node[1]})
	}
	return validSibling
}

func isNodeInPath(node [2]int, path [][2]int) bool {
	for _, n := range path {
		if n[0] == node[0] && n[1] == node[1] {
			return true
		}
	}
	return false
}

func minimumEffortPath(heights [][]int) int {
	lenX := len(heights)
	lenY := len(heights[0])

	endNode := [2]int{len(heights) - 1, len(heights[0]) - 1}

	finalPaths := [][][2]int{}

	// append startNode to allPossiblePaths
	allPossiblePaths := [][][2]int{
		[][2]int{
			[2]int{0, 0},
		},
	}

	for len(allPossiblePaths) != 0 {
		newAllPossiblePaths := [][][2]int{}
		for _, path := range allPossiblePaths {
			lastNode := path[len(path)-1]
			for _, siblingNode := range getValidSiblings(lastNode, lenX, lenY) {
				if isNodeInPath(siblingNode, path) {
					continue
				}
				if siblingNode[0] == endNode[0] && siblingNode[1] == endNode[1] {
					fmt.Printf("final hit: %d, %d\n", siblingNode[0], siblingNode[1])
					finalPaths = append(finalPaths, append(path, siblingNode))
				} else {
					newAllPossiblePaths = append(newAllPossiblePaths, append(path, siblingNode))
				}
			}
		}
		allPossiblePaths = newAllPossiblePaths
	}
	for _, path := range finalPaths {
		pathStr := ""
		for _, node := range path {
			pathStr = fmt.Sprintf("%s -> %d,%d", pathStr, node[0], node[1])
		}
		fmt.Println(pathStr)
	}
	fmt.Println(endNode)
	return 1
}

func main() {
	heights := [][]int{
		[]int{1, 2, 2},
		[]int{3, 8, 2},
		[]int{5, 3, 5},
	}
	minimumEffortPath(heights)
}
