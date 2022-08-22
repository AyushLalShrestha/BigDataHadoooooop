package main

import "fmt"

func maxProfit(prices []int) int {
	maxProfit := 0
	var minimumPrice int
	for i, price := range prices {
		if i == 0 {
			minimumPrice = price
			continue
		}
		if price < minimumPrice {
			minimumPrice = price
		} else if price-minimumPrice > maxProfit {
			maxProfit = price - minimumPrice
		}
	}
	return maxProfit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	prices = []int{7, 6, 4, 3, 1}
	res := maxProfit(prices)
	fmt.Println(res)
}
