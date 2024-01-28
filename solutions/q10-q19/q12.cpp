#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int count_divisors(int n) {
    int total = 1;
    for (int i = 2; i <= sqrt(n); ++i) {
        int count = 0;
        while (n % i == 0) {
            ++count;
            n /= i;
        }
        total *= (count + 1);
    }
    if (n > 1) total *= 2; 
    return total;
}

int main() {
    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        int n = 1;
        int L = 1;
        int numDivisors = 0;
        while (numDivisors <= N) {
            L = n * (n + 1) / 2;
            int count = 0;
            if (n % 2 == 0) {
                count = count_divisors(n/2) * count_divisors(n+1);
            } else {
                count = count_divisors(n) * count_divisors((n+1)/2);
            }
            numDivisors = count;
            ++n;
        }
        cout << L << endl;
    }
    return 0;
}
