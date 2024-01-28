#include <iostream>
#include <vector>
using namespace std;

int sod(vector<int>& number) {
    int sum = 0;
    for (int digit : number) {
        sum += digit;
    }
    return sum;
}

int main() {
    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        vector<int> result = {1};
        for (int i = 0; i < N; i++) {
            int carry = 0;
            for (int j = 0; j < result.size(); j++) {
                int temp = result[j] * 2 + carry;
                result[j] = temp % 10;
                carry = temp / 10;
            }
            while (carry) {
                result.push_back(carry % 10);
                carry /= 10;
            }
        }
        cout << sod(result) << endl;
    }
    return 0;
}
