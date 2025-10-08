package main

import (
	"fmt"
	"slices"
)

func main() {
	s := []string{"a", "b", "c", "d", "e", "f"}

	l := s[:5] //1
	fmt.Println("sl2:", l)

	l = s[2:] //2
	fmt.Println("sl3:", l)

	t := []string{"g", "h", "i"} //3
	fmt.Println("dcl:", t)

	t2 := []string{"g", "h", "i"} //4
	if slices.Equal(t, t2) {
		fmt.Println("t == t2")
	}

	twoD := make([][]int, 3) //5
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}

	fmt.Println("2d:", twoD)
}