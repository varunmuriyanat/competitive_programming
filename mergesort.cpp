#include <iostream>

using namespace std;

void merge_sort(int [], int, int);
void merge(int [], int, int, int);

int main() {
    int n = 8;
    int foo[n] = {14, 7, 3, 12, 9, 11, 6, 2}; 

    for(int i=0; i<n; i++) {
        cout << foo[i] << " ";
    }
    cout << endl;

    merge_sort(foo, 0, n-1);

    for(int i=0; i<n; i++) {
        cout << foo[i] << " ";
    }
    cout << endl;
}

void merge_sort(int a[], int start, int end) {
    cout << "start = " << start << " end = " << end << endl;
    if(start < end) {
        int mid = (start + end) / 2;
        merge_sort(a, start, mid);
        merge_sort(a, mid + 1, end);
        //merge(a, start, mid, end);
    }
}

void merge(int a[], int start, int mid, int end) {
    int p = start, q = (mid + 1)/2;
    int arr[end-start+1], k=0;

    //for(int i = start; i <= end; i++) {
    //    if(p > mid)
    //        arr[k++] = a[q++];

    //}

    for(int p = 0; p < end-start;) {

    }
}

