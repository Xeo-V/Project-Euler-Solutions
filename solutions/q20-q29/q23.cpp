#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 100000;

vector<bool> is_abundant(MAX_N+1, false);
vector<int> abundant_numbers;

void precompute_abundant_numbers() {
    for (int i = 1; i <= MAX_N; ++i) {
        int sum = 1; 
        for (int j = 2; j*j <= i; ++j) {
            if (i % j == 0) {
                sum += j;
                if (i/j != j) sum += i/j;
            }
        }
        if (sum > i) {
            is_abundant[i] = true;
            abundant_numbers.push_back(i);
        }
    }
}

bool check_sum_of_abundants(int n) {
    if (n < 24) return false; 
    for (int i = 0; abundant_numbers[i] <= n/2; ++i) {
        if (is_abundant[n - abundant_numbers[i]]) return true;
    }
    return false;
}

int main() {
    precompute_abundant_numbers();
    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        cout << (check_sum_of_abundants(N) ? "YES" : "NO") << endl;
    }
    return 0;
}
