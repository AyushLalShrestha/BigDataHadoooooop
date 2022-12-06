package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	inputData, _ := os.ReadFile("input")
	inputInstructionData, _ := os.ReadFile("input-ins")
	inputs := strings.Split(string(inputData), "\n")
	inputInstructions := strings.Split(string(inputInstructionData), "\n")

	// Parse the input data
	cols := (len(inputs[0]) + 1) / 4
	stacks := make([][]string, cols)
	for j := range inputs {
		line := inputs[len(inputs)-j-1]
		lineArr := strings.Split(line, "")
		i := 0
		for i < len(lineArr) {
			val := lineArr[i+1]
			if val != " " {
				stacks[i/4] = append(stacks[i/4], val)
			}
			i += 4
		}
	}

	// Parse the input instructions
	instructions := [][3]int{}
	for _, instructionLine := range inputInstructions {
		parts := strings.Split(instructionLine, " ")
		moves, _ := strconv.Atoi(parts[1])
		from, _ := strconv.Atoi(parts[3])
		to, _ := strconv.Atoi(parts[5])
		instruction := [3]int{moves, from, to}
		instructions = append(instructions, instruction)
	}

	// Make the moves
	for _, instruction := range instructions {
		moves := instruction[0]
		from := instruction[1]
		to := instruction[2]
		for i := 0; i < moves; i++ {
			_from := stacks[from-1]
			val := _from[len(_from)-1]
			stacks[from-1] = _from[:len(_from)-1]
			stacks[to-1] = append(stacks[to-1], val)
		}
	}

	// Output
	output := ""
	for _, s := range stacks {
		output += s[len(s)-1]
	}
	fmt.Println(output)

}
