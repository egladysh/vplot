#include <iostream>
#include <vector>
#include <cmath>

int main()
{
	std::cout << "Hi" << std::endl;

	std::vector<double> test_vect;
	for (int i = 0; i < 1000; ++i) {
		test_vect.push_back(std::cos(static_cast<double>(i)/100.));
	}

	std::vector<double> test_vect1;
	for (int i = 0; i < 1000; ++i) {
		test_vect1.push_back(0.5*std::cos(static_cast<double>(i)/10.));
	}

	return 0;
}
