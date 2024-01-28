#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N, Q;
    cin >> N;
    vector<string> names(N);
    for(int i = 0; i < N; ++i) {
        cin >> names[i];
    }
    sort(names.begin(), names.end());

    cin >> Q;
    while(Q--) {
        string query;
        cin >> query;
        auto it = find(names.begin(), names.end(), query);
        int position = distance(names.begin(), it) + 1;
        int score = 0;
        for(char c : query) {
            score += c - 'A' + 1;
        }
        cout << score * position << endl;
    }
    return 0;
}
