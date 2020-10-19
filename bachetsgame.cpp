#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;


int main() {
    int n, m;
    while (cin >> n >> m) {
        vector<int> moves;

        vector<bool> winning;
        winning.push_back(false);

        for (int i = 0; i < m; i++) {
            int move;
            cin >> move;
            moves.push_back(move);
        }

        sort(moves.begin(), moves.end());

        for (int i = 1; i <= n;i++) {
            bool found = false;
            for (auto it = begin(moves); it != end(moves); it++) {
                if (*it > i) {
                    winning.push_back(false);
                    found = true;
                    break;
                }
                if (!winning[i - *it]) {
                    winning.push_back(true);
                    found = true;
                    break;
                }
            }
            if (found == false) {
                winning.push_back(false);
            }
        }

        if (winning.back()) {
            cout << "Stan wins" << endl;
        }
        else {
            cout << "Ollie wins" << endl;
        }
    }
}