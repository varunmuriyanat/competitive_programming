#include <iostream>
#include <iomanip>
//#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 5;
    int value[n][n] = {{3, 7, 9, 2,  7},
                       {9, 8, 3, 5,  5},
                       {1, 7, 9, 8,  5},
                       {3, 8, 6, 4, 10},
                       {6, 3, 9, 7,  8}};

    // 3 10 19 21 28
    //12 20 23 28 33
    //13 27 36 44 49
    //16 35 42 48 59
    //22 38 51 58 67

    int sum[n][n] = {};

    cout << "Original array values" << endl;
    for(int y = 0; y < n; y++) {
        for(int x = 0; x < n; x++) {
            cout << setfill(' ') << setw(2) << value[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;

    cout << "Values before initialization" << endl;
    for(int y = 0; y < n; y++) {
        for(int x = 0; x < n; x++) {
            cout << setfill(' ') << setw(2) << sum[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;


    for(int y = 0; y < n; y++) {
        for(int x = 0; x < n; x++) {
           sum[y][x] = max(sum[y][max(x-1, 0)], sum[max(y-1, 0)][x]) + value[y][x]; 
        }
    }

    cout << "Values after initialization" << endl;
    for(int y = 0; y < n; y++) {
        for(int x = 0; x < n; x++) {
            cout << setfill(' ') << setw(2) << sum[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

