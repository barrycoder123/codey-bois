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
#include <string>
#include <algorithm>
#include <vector> 

template<typename T>
void merge_sort(std::vector<T>& arr);
template<typename A>
void merge(std::vector<A>& left, std::vector<A>& right, std::vector<A>& results);

int main() {
    std::vector<int> my_vector{10, 50, 100, 40};
    merge_sort(my_vector);
    for (int i: my_vector) {
        std::cout << i << std::endl;
    }
    std::vector <char> my_str{'a', 'c', 'b', 'g', 'q'};
    merge_sort(my_str);
    // my_str.erase(unique(my_str.begin(), my_str.end()));

    for (char i: my_str) {
        std::cout << i << std::endl;
    }
    
}

// but we can sort not only integers: use templates
template<typename T> 
void merge_sort(std::vector<T>& arr) {
    if (arr.size() <= 1) return;

    int mid = arr.size() / 2;
    std::vector<T> left(arr.begin(), arr.end() - mid);
    std::vector<T> right(arr.begin() + mid, arr.end());

    merge_sort(left);
    merge_sort(right);
    merge(left, right, arr);
}
// instead of using twice the size of the current array use only 1 times the current size:
// to do this use allocated the memory needed once outside the merge_sort function and then pass in this memory into the function
template<typename I>
void merge_buffer(std::vector<I>& arr) {
    std::vector <int> tmp_mem(arr.size());
    merge_sort(arr);
}
template<typename A>
void merge(std::vector<A>& left, std::vector<A>& right, std::vector<A>& results) {
    int L_size = left.size();
    int R_size = right.size();
    int i = 0, j = 0, k = 0;
    // two finger algorithm
    while (j < L_size && k < R_size) 
    {
        if (left[j] <= right[k]) {
            results[i] = std::move(left[j]);
            j++;
        }
        else {
            results[i] = std::move(right[k]);
            k++;
        }
        i++;
    }
    // its easier to use standard algos from STL
    std::move(&left[j],  &left[L_size],  &results[i]);
    std::move(&right[k], &right[R_size], &results[i]);
}




















