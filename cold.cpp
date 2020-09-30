#include <iostream>

int main() {
	//takes first argument number of temperatures so that I know how much I should loop
	int ntemps;
	std::cin >> ntemps;

	//number of temps sub zero
	int nsubzero = 0;
	
	for (int i = 0; i < ntemps; i++) {
		int temp;
		std::cin >> temp;

		//if user input number is less than 0, incremment var
		if (temp < 0) {
			nsubzero++;
		}
	}
	std::cout << nsubzero;
	return 0;
}