package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var digits []int

	for scanner.Scan() {
		digit, _ := strconv.Atoi(scanner.Text())
		digits = append(digits, digit)
	}

	result_1 := part1(digits)
	result_2 := part2(digits)

	fmt.Println(result_1)
	fmt.Println(result_2)
}

func part1(digits []int) int {
	result := 0

	for idx, digit := range digits[1:] {
		if digit > digits[idx] {
			result++
		}
	}
	return result
}

func part2(digits []int) int {
	result := 0

	for idx, digit := range digits[3:] {
		if digit > digits[idx] {
			result++
		}
	}
	return result
}
