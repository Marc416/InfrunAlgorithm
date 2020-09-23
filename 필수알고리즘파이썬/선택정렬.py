# http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html
arr = [1,3,2,5,4]

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # arr[min_idx] = arr[i]

selection_sort(arr)
print(arr)