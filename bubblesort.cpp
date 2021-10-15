#include <iostream>

using namespace std;

int main() {
    int n = 8;
    int foo[n] = {14, 7, 3, 12, 9, 11, 6, 2}; 

    for(int i=0; i<n; i++) {
        for(int j=0; j<n-1; j++) {
            if(foo[i]<foo[j])
                swap(foo[i], foo[j]);
        }
    }

    for(int i=0; i<n; i++) {
        cout << foo[i] << " ";
    }
    cout << endl;
}
 