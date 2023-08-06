package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines [][]string

	for scanner.Scan() {
		var s = strings.Split(scanner.Text(), "")
		lines = append(lines, s)
	}

	fmt.Println(count_trees(lines, 3, 1))                                                                                                             // Part 1
	fmt.Println(count_trees(lines, 1, 1) * count_trees(lines, 3, 1) * count_trees(lines, 5, 1) * count_trees(lines, 7, 1) * count_trees(lines, 1, 2)) // Part 2
}

func count_trees(lines [][]string, right int, down int) int {
	var x = 0
	var y = 0
	var count = 0

	for y < len(lines) {
		if lines[y][x%len(lines[0])] == "#" {
			count++
		}
		x += right
		y += down
	}

	return count

}
