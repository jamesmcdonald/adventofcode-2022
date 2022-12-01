package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func readinput(filename string) (int, int, int) {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var cur, max, mx2, mx3 int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		t := scanner.Text()
		if t == "" {
			fmt.Println(cur, max, mx2, mx3)
			if cur >= max {
				mx3 = mx2
				mx2 = max
				max = cur
			} else if cur >= mx2 {
				mx3 = mx2
				mx2 = cur
			} else if cur >= mx3 {
				mx3 = cur
			}

			cur = 0
		}

		if val, err := strconv.Atoi(t); err == nil {
			cur += val
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return max, mx2, mx3
}

func main() {
	max, mx2, mx3 := readinput("input")
	fmt.Println(max, max+mx2+mx3)
}
