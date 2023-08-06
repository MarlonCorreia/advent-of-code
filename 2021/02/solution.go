package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var commands []map[string]int

	for scanner.Scan() {
		command := make(map[string]int)
		text := scanner.Text()
		spllited := strings.Split(text, " ")

		digit, _ := strconv.Atoi(spllited[1])

		command[spllited[0]] = digit
		commands = append(commands, command)

	}

	result_1 := part1(commands)
	result_2 := part2(commands)

	fmt.Println(result_1)
	fmt.Println(result_2)
}

func part1(commands []map[string]int) int {
	depth := 0
	hor := 0

	for _, val := range commands {
		for key, elem := range val {
			if key == "forward" {
				hor += elem
			} else if key == "down" {
				depth += elem
			} else {
				depth -= elem
			}

		}
	}
	return depth * hor

}

func part2(commands []map[string]int) int {
	depth := 0
	hor := 0
	aim := 0

	for _, val := range commands {
		for key, elem := range val {
			if key == "forward" {
				hor += elem
				depth += aim * elem
			} else if key == "down" {
				aim += elem
			} else {
				aim -= elem
			}
		}
	}

	return depth * hor
}
