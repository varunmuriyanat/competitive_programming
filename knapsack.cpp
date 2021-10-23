#include <iostream>
#include <iomanip>
//#include <bits/stdc++.h>

using namespace std;

int main() {

    int n = 13;
    int k = 4;
    int w[k] = {1, 3, 3, 5};

    bool possible[n][k] = {{false},{false}};

    // initialize the array
    for(int y = 0; y < n; y++) {
        for(int x = 0; x < k; x++) {
            possible[y][x] = false;
        }
    }

    // print array
    for(int x = 0; x < k; x++) {
        cout << w[x] << " ";
    }
    cout << endl << endl;

    // print the boolean array
    for(int y = 0; y < n; y++) {
        for(int x = 0; x < k; x++) {
            cout << possible[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
    cout << endl;


    possible[0][0] = true;
    //for(int k = 0; k < n; k++) {
    //    for(int x = 0; x < m; x++) {
    //        if(x-w[k] >= 0) {
    //            possible[x][k] |= possible[x-w[k]][k-1];
    //        }
    //        possible[x][k] |= possible[x][k-1];
    //    }
    //}

    for(int y = 0; y < n; y++) {
        for(int x = 0; x < k; x++) {
            cout << possible[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

