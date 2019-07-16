# TO-DO: Complete the selection_sort() function below 
arrlist = [21, 3, 899, 43, 65]
def swap(smallest, cur_ind):
    temp = arrlist[smallest]
    arrlist[smallest] = arrlist[cur_ind]
    arrlist[cur_ind] = temp

def selection_sort( arr ):
    # loop through n-1 elements
    print(f'{len(arr) - 1}')
    for i in range(0, len(arr) - 1): #only want the index of each number that's why we do len - 1
        cur_index = i
        smallest_index = cur_index
        # find next smallest element
        for j in range(cur_index, len(arr)): #why doesn't it work if len - 1 
            print(f'is {arr[j]} > {arr[smallest_index]}')

            if  arr[smallest_index] > arr[j]: #here we are checking the items in the 
                smallest_index = j
                
     #TO DO: swap
        # temp = arr[smallest_index]
        # arr[smallest_index] = arr[cur_index]
        # arr[cur_index] = temp
        swap(smallest_index, cur_index)
       
    return arr

sortlist = selection_sort(arrlist)
print(sortlist)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        #get the current index and compare if with the num next to it
        for j in range(0, len(arr) - i - 1):
             if arr[j] > arr[j + 1]:
                 #print(f'is {arr[j]} > {arr[j + 1]}')
                 arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([32, 1, 87, 44]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


