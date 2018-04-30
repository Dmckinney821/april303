def bubble_sort(arr):


input_array = [[], [1, 3, 6, 2, 6, 3, 2, 4]]
sorted_array = [[], [1, 2, 2, 3, 3, 4, 6, 6]]

for i in range(len(input_array)):
    print('')
    print(' Input: ' + str(input_array[i]))
    output_array = bubble_sort(input_array[i])
    print('Output: ' + str(output_array))
    test_passed = 'true' if output_array == sorted_arrays[i] else ' false'
    print('test passed?' + test_passed)

