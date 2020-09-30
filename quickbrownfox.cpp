#include <iostream>
#include <string>
#include <array>

int main() {
	//takes first argument number of phrases so that I know how much I should loop
	int n_phrase;
	std::cin >> n_phrase;
	//clear buffer to avoid conflicts with getline
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	//initialize an array containing all the ascii codes of lower case alphabet in alphabetical order ex: alphabet[0]=97, (char)97=a
	std::array<int, 26> alphabet{};
	for (int c{ 0 }; c < alphabet.size(); c++ ) {
		alphabet[c] = c + 97;
	}

	for (int i = 0; i < n_phrase; i++) {
		//increments each time a new letter is FIRST encountered when iterating through the phrase
		int unique_c = 0;

		std::string phrase;
		std:getline (std::cin,phrase);

		//copy of the alphabet, use for flagging down letters encountered
		std::array<int,26> c_phrase = alphabet;
		for (char& c : phrase) {
			//lowercase each letter in the sentence, correct for the offset of the ASCII(97) to make it correspond to the index of the array, flag down the position to 0
			c = std::tolower(c);
			if (c >= 97 && c <= 122) {
				if (c_phrase[c - 97] != 0) {
					c_phrase[c - 97] = 0;
					unique_c++;
				}
			}
		}
		//if more than 25 unique letters appeared, it's a pangram
		if (unique_c > 25) {
			std::cout << "pangram" << std::endl;
		}
		//else iterate through the alphabet array, printing the letters not flagged down
		else {
			std::cout << "missing ";
			for (int c{ 0 }; c < c_phrase.size(); c++) {
				if (c_phrase[c] != 0) {
					std::cout << (char)c_phrase[c];
				}
			}
			std::cout << std::endl;
		}
	}
	return 0;
}