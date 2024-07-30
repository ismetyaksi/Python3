### Bubble Sort

- Bubble sort is a simple sort algorithm.
- Adjacent elements of a list are compared.
- They are swapped if they are in the wrong order.

Python3 program performs bubble sort 4 times.

1. Sort list in ascending order.
2. Sort list in ascendig order with optimization.
    - In optimization, inner loop swaps are flagged. If there is no inner loop swap is performed, list is already sorted and algorithm terminated. 

    - The number of iterations is usually less, except in worst case scenarios.
3. Sort list in descending order.
4. Sort list in descending order with optimization.

#### Following is detailed explanation of program.

- List is initialized using __init_list__ function. Number of elements and type of order are specified as parameters.
- __ascending__ parameter prepares list before descending order for worst case scenario.
- __descending__ parameter prepares list before ascending order for worst case scenario.
- __random__ parameter prepares list with random elements.
- __seed__ specified for preparing same list for all sorts.
- __Number of iterations__ and __number of swaps__ counters are initialized for each sort.
- Outer loop starts executing from bottom element. Inner loop starts from outer loop index up to first element.
- Adjacent elements are tested for order and swapped if they are in wrong order.
- After completing sorting, Python3 __sort__ command is used for verifying implemented algorithm.
- For optimized implementations __number of inner swaps__ reset before inner loop and set if occurs. At he end of inner loop, sorting terminated if no swaps occurred.

#### Following is sample output for a 1.000 element list.

0 >>> list size.. 1,000

1 >>> sort ascending

1 >>> #iterations 499,500
1 >>> #swaps..... 256,297

1 >>> sort ascending optimized

1 >>> #iterations 499,269
1 >>> #swaps..... 256,297

2 >>> sort descending

2 >>> #iterations 499,500
2 >>> #swaps..... 242,729

2 >>> sort descending optimized

2 >>> #iterations 497,609
2 >>> #swaps..... 242,729

