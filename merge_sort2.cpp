// will write a program for merge sort
/* steps:
 * have an array of size n call it A
 * divide A into left and right halves L and R
 * call merge sort on the two halves now L' and R'
 * now merge the two halves into B (the sorted version of A)
 */
/* the merging algorithm:
 * the merging algorithm is a "two finger algo"
 * where an element of L' is compared with each elt of R' until the elt in R' is less
 * we then take this element and put it into our sorted array, B
 */
#include <iostream>
#include <vector> // will use the vector class  to make things like list slicing very easy

using namespace std;
void merge_sort(vector<int> &arr);
void merge(vector<int >&left, vector<int> &right, vector<int> &results);

int main() {
    vector<int> my_vector{10, 30, 50, 40};
    merge_sort(my_vector);

    for (int i: my_vector)
        cout << i << ',';
    return 0;
}

void merge_sort(vector<int> & arr) {
    if (arr.size() <= 1) return;

    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.end() - mid);
    vector<int> right(arr.begin() + mid, arr.end());

    merge_sort(left);
    merge_sort(right);
    merge(left, right, arr);
}
void merge(vector<int> &left, vector<int> &right, vector<int> &results)
{
    int L_size = left.size();
    int R_size = right.size();
    int i = 0, j = 0, k = 0;
    // two finger algorithm
    while (j < L_size && k < R_size) 
    {
        if (left[j] < right[k]) {
            results[i] = left[j];
            j++;
        }
        else {
            results[i] = right[k];
            k++;
        }
        i++;
    }
    while (j < L_size) {
        results[i] = left[j];
        j++; i++;
    }
    while (k < R_size) {
        results[i] = right[k];
        k++; i++;
    }
}




















