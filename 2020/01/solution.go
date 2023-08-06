package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var target = 2020

func main() {
	part1()
	part2()

}

func part1() {
	var ids = make(map[int]int)
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text())
		ids[line] = line

		if val, boo := ids[target-line]; boo && val != line {
			fmt.Println(val * line)
			return
		}
	}

	file.Close()
}

func part2() {
	var ids = make(map[int]int)
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text())
		ids[line] = line

		for value := range ids {

			if val, boo := ids[target-line-value]; boo {
				fmt.Println(line * value * val)
				return
			}
		}
	}

	file.Close()

}
