package main

import (
	"fmt"
	"time"
)

func testcount(x int) int {
	if x == 1000000 {
		return 0
	}
	fmt.Println(x)
	return testcount(x + 1)
}

func main() {
	start := time.Now() // išsaugome pradžios laiką

	testcount(1)

	elapsed := time.Since(start) // apskaičiuojame praėjusį laiką
	fmt.Printf("Kodo vykdymas užtruko: %s\n", elapsed)
}