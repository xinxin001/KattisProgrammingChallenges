
#include <iostream>

int main() {
	//takes first argument number of tests so that I know how much I should loop
	int tests;
	std::cin >> tests;

	for (int i = 0; i < tests; i++) {
		//test number
		int integer;
		std::cin >> integer;

		//limited int to be between -10 and 10 in the problem rules
		if (integer >= -10 && integer <= 10) {
			//if the int modulo is 0, it's even, else it's odd.
			if (integer % 2 == 0) {
				std::cout << integer << " is even \n";
			}
			else {
				std::cout << integer << " is odd \n";
			}
		}
	}
	return 0;
}
