#include <iostream>
#include <iomanip>
//#include <bits/stdc++.h>

using namespace std;

int main() {

    int n = 13;
    int k = 5;
    //int w[k] = {0, 1, 3, 3, 5};

    bool possible[n][k] = {{false},{false}};
    for(int y = 0; y < n; y++) { 
        for(int x = 0; x < k; x++) {
            possible[x][y] = 0;
        }
    }

    for(int y = 0; y < n; y++) { 
        for(int x = 0; x < k; x++) {
            cout << setfill(' ') << setw(2) << possible[x][y] << " ";
        }
        cout << endl;
    }
    cout << endl;
}


