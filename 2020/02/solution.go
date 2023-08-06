package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var result_1 = 0
var result_2 = 0

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		var line = scanner.Text()
		var letter = strings.Trim(strings.Split(line, " ")[1], ":")
		var passw = strings.Split(line, " ")[2]
		var min, _ = strconv.Atoi(strings.Split(strings.Split(line, " ")[0], "-")[0])
		var max, _ = strconv.Atoi(strings.Split(strings.Split(line, " ")[0], "-")[1])

		part1(letter, passw, min, max)
		part2(letter, passw, min, max)
	}

	fmt.Println(result_1)
	fmt.Println(result_2)
}

func part1(letter string, passw string, min int, max int) {
	if strings.Count(passw, letter) >= min && strings.Count(passw, letter) <= max {
		result_1++
	}
}

func part2(letter string, passw string, min int, max int) {
	if (string(passw[min-1]) == letter && string(passw[max-1]) != letter) || (string(passw[min-1]) != letter && string(passw[max-1]) == letter) {
		result_2++
	}
}
