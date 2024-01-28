#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string getPermutation(int n) {
    string s = "abcdefghijklm";
    string result;
    int size = s.size();
    --n; 

    vector<int> factors(size, 1); 

    for (int i = 1; i < size; ++i) {
        factors[i] = factors[i - 1] * i;
    }

    for (int i = size; i > 0; --i) {
        int index = n / factors[i - 1];
        n %= factors[i - 1];
        result.push_back(s[index]);
        s.erase(s.begin() + index);
    }

    return result;
}

int main() {
    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        cout << getPermutation(N) << endl;
    }
    return 0;
}
