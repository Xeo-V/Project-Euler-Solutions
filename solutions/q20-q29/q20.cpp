#include <iostream>
#include <vector>

using namespace std;

vector<int> factorial(int N) {
    vector<int> result(1,1);
    for (int x = 2; x <= N; x++) {
        int carry = 0;
        for (int i = 0; i < result.size(); i++) {
            int prod = result[i] * x + carry;
            result[i] = prod % 10;
            carry = prod / 10;
        }
        while (carry) {
            result.push_back(carry % 10);
            carry /= 10;
        }
    }
    return result;
}

int sumOfDigits(int N) {
    vector<int> digits = factorial(N);
    int sum = 0;
    for (int digit : digits)
        sum += digit;
    return sum;
}

int main() {
    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        cout << sumOfDigits(N) << endl;
    }
    return 0;
}
