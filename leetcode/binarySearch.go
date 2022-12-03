package main

import "fmt"

func search(nums []int, target int) int {
	start := 0
	end := len(nums) - 1

	for {
		oldStart := start
		oldEnd := end
		if nums[start] == target {
			return start
		}
		if nums[end] == target {
			return end
		}
		midIndex := (end + start) / 2
		midValue := nums[midIndex]

		if midValue == target {
			return midIndex
		} else if midValue > target {
			end = midIndex
		} else if midValue < target {
			start = midIndex
		}
		if start == oldStart && end == oldEnd {
			break
		}
	}
	return -1
}

func main() {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 9

	nums = []int{-1, 0, 3, 5, 9, 12}
	target = 2
	fmt.Println(search(nums, target))
}
