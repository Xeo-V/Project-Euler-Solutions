#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<vector<int>> triangle(N, vector<int>());
        
        for (int i = 0; i < N; ++i) {
            triangle[i].resize(i + 1);
            for (int j = 0; j <= i; ++j) {
                cin >> triangle[i][j];
            }
        }
        
        for (int i = N - 2; i >= 0; --i) {
            for (int j = 0; j <= i; ++j) {
                triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        
        cout << triangle[0][0] << endl;
    }
    return 0;
}
