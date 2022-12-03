package main

import (
	"fmt"
)

func canConstruct(ransomNote string, magazine string) bool {
	count := make(map[string]int)

	for _, s := range magazine {
		count[string(s)] += 1
	}

	for _, s := range ransomNote {
		if val, ok := count[string(s)]; ok {
			if val <= 0 {
				return false
			}
			count[string(s)] -= 1
		} else {
			return false
		}
	}
	return true

}

func main() {
	// ransomNote := "aa"
	// magazine := "aab"
	ransomNote := "aa"
	magazine := "ab"

	fmt.Println(canConstruct(ransomNote, magazine))
}
