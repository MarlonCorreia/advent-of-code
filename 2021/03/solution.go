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
	var digits []string

	for scanner.Scan() {
		digits = append(digits, scanner.Text())
	}

	part1 := part1(digits)

	fmt.Println(part1)
}

func part1(digits []string) int {
	result := 0
	var commons [][]int

	for _, value := range digits {
		for i := 0; i < len(value); i++ {
			var cur []int
			if len(commons) > i {
				cur = commons[i]
			}
			v, _ := strconv.Atoi(string(value[i]))
			cur = append(cur, v)

			if len(commons) > i {
				commons[i] = cur
			} else {
				commons = append(commons, cur)
			}
		}
		fmt.Println(commons)
	}
	return result
}
