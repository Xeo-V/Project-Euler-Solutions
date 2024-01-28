#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int main() {
    int N, a_max = 0, b_max = 0, n_max = 0;
    cin >> N;

    for (int a = -N; a <= N; ++a) {
        for (int b = -N; b <= N; ++b) {
            int n = 0;
            while (is_prime(n * n + a * n + b)) {
                ++n;
            }
            if (n > n_max) {
                a_max = a;
                b_max = b;
                n_max = n;
            }
        }
    }

    cout << a_max << " " << b_max << endl;
    return 0;
}
