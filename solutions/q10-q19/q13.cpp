#include <iostream>
#include <vector>
#include <string>

int main() {
    int N;
    std::cin >> N;

    std::string number;
    std::vector<long long> sum(50, 0);

    for (int i = 0; i < N; ++i) {
        std::cin >> number;
        for (int j = 0; j < 50; ++j) {
            sum[j] += (number[j] - '0');
        }
    }

    for (int i = 49; i > 0; --i) {
        sum[i - 1] += sum[i] / 10;
        sum[i] %= 10;
    }

    std::string result;
    for (auto digit : sum) {
        result += std::to_string(digit);
    }
    std::cout << result.substr(0, 10) << std::endl;

    return 0;
}
