def quickSort(array):
	if len(array) < 2:
		return array ## Base Case :  arrays with 0 or 1 element are already "sorted".
	else:
		pivot  = array[0]
		less = [i for i in array[1:] if i <= pivot] # Sub-array of all the elements less than the pivot
		greater = [i for i in array[1:] if i > pivot] # Sub-array of all the elements greater than the pivot
		return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10, 5, 2, 3]))
