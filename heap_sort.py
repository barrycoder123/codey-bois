'''
program to do heap_sort from MIT OCW lecture 4:
look at heap_sort.txt for more details

'''
import math
def max_heapify(A, i, n):
    '''
        args:(A, i) heap A and index i
        correct a single violation of MHP at subroot's tree
    '''
    # find the left and right tree
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and A[i] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    if largest !=i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)


def build_max_heap(A):
    '''
        Args: A-array
        return val: heapified Array A
    '''
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, i, n)
    return A


def heap_sort(A):
    '''
        Args: A max heap
        Return val: A list that is sorted
    '''
    build_max_heap(A)
    # swap A[n] with A[i]
    n = len(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, 0, i)
    return A

if __name__ == '__main__':
    my_A = [-9343, 424, 343, 13, 4324343]
    my_ans = heap_sort(my_A)
    print(my_ans)



















