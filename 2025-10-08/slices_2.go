package main

import (
	"fmt"
)

func main() {
	var s []string
	s = make([]string, 5)

	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	s[3] = "d"
	s[4] = "e"
	
	fmt.Println("set:", s)

	fmt.Println("len:", len(s)) //1

	s = append(s, "d")           //2
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	c := make([]string, len(s))  //3
	copy(c, s)
	fmt.Println("cpy:", c)

	l := s[2:5] //4
	fmt.Println("s1:", l)
}