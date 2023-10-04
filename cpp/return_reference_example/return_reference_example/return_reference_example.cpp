#include <iostream>

// global variable
int num;

// function definition
// returns the address of num variable
int& test() {
	return num;
}


int main() {

	// assign 5 to num variable
	// equivalent to num = 5;
	test() = 5;

	std::cout << num;

	return 0;
}