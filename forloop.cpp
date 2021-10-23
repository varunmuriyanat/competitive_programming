#include <iostream>
#include <iomanip>
//#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 2, k = 3;
    int possible[n][k] = {{1,2,3}, 
                          {4,5,6}};

    bool b[n][k] = {{false}, {false}};

    for(int y = 0; y < n; y++) {
        for(int x = 0; x < k; x++) {
            cout << possible[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;

    for(int y = 0; y < n; y++) {
        for(int x = 0; x < k; x++) {
            cout << b[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;

}

