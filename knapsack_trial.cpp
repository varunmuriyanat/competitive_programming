#include <iostream>
#include <iomanip>
//#include <bits/stdc++.h>

using namespace std;

int main() {

    int n = 13;
    int k = 5;
    int w[k] = {0, 1, 3, 3, 5};

    bool possible[n][k] = {{false},{false}};

    // initialize the array
    for(int x = 0; x < k; x++) {
        for(int y = 0; y < n; y++) {
            possible[y][x] = false;
        }
    }

    // print the weights array
    for(int x = 0; x < k; x++) {
        cout << setfill(' ') << setw(2) << w[x] << " ";
    }
    cout << endl << endl;

    // print the boolean array
    for(int x = 0; x < k; x++) {
        for(int y = 0; y < n; y++) {
            cout << setfill(' ') << setw(2) << possible[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
    cout << endl;

    int sum = 0;
    for(int y = 1; y < n; y++) {
        sum = 0;
        for(int x = 1; x < k; x++) {
            if(w[x] <= y) {
                sum += w[x];
                cout << setfill(' ') << setw(8) << y << "," << w[x] << "," << sum;
            }
        }
        cout << endl;
    }
    cout << endl;

    //print the boolean array again
    for(int x = 0; x < k; x++) {
        for(int y = 0; y < n; y++) {
            cout << setfill(' ') << setw(2) << possible[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
}


