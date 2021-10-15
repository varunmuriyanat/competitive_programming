//#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 8;
    int array[n] = {6, 2, 5, 1, 7, 4, 8, 3};
    int length[n] = {};

    for(int k = 0; k < n; k++) {
        length[k] = 1;
        for(int i = 0; i < k; i++) {
            if (array[i] < array[k]) {
                length[k] = max(length[k], length[i] + 1);
            }
        }
    }

    for(int k = 0; k < n; k++) {
        cout << array[k] << " ";
    }
    cout << endl;

    cout << "The length of the longest increasing subsequence that ends at position k" << endl;
    for(int k = 0; k < n; k++) {
        cout << length[k] << " ";
    }
    cout << endl;
}

