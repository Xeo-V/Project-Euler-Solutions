#include <iostream>
#include <vector>
#include <unordered_map>

const int LIMIT = 5 * 1e6;
std::vector<int> sequence_length(LIMIT + 1, 0);

int collatz_sequence_length(long long n) {
    if (n == 1) return 1;
    if (n <= LIMIT && sequence_length[n] != 0) return sequence_length[n];

    int length = 0;
    if (n % 2 == 0) {
        length = 1 + collatz_sequence_length(n / 2);
    } else {

        if (n <= (LIMIT - 1) / 3) {
            length = 1 + collatz_sequence_length(3 * n + 1);
        } else {

            length = 1 + collatz_sequence_length(3 * n + 1);
        }
    }

    if (n <= LIMIT) sequence_length[n] = length;
    return length;
}

int main() {
    int T;
    std::cin >> T;

    sequence_length[1] = 1;
    for (int i = 2; i <= LIMIT; ++i) {
        collatz_sequence_length(i);
    }

    std::vector<int> max_number(LIMIT + 1, 0);
    int max_len = 0, number = 0;
    for (int i = 1; i <= LIMIT; ++i) {
        if (sequence_length[i] >= max_len) {
            max_len = sequence_length[i];
            number = i;
        }
        max_number[i] = number;
    }

    while (T--) {
        int N;
        std::cin >> N;
        std::cout << max_number[N] << std::endl;
    }

    return 0;
}
