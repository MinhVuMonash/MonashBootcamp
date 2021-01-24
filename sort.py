#The sort_function will sort the array in ascending order
#The function will find the smallest element in the list and append it to the new array while
#removing that element from the original array

def sort_function(array_to_sort):
    aLst = array_to_sort
    sorted_lst =[]
    array_length = len(aLst)
    #The loop will run until sorted_lst have the same length as the array that need to be sorted
    while(len(sorted_lst) < array_length):
        min_elem = aLst[0]
        curr_array_length = len(aLst)
        #Assigning the first element in the array as the smallest number
        #The for loop iterate through the array and find the smallest element 
        for i in range(curr_array_length):
            curr_val = aLst[i]
            if (min_elem >= aLst[i]):
                min_elem = aLst[i]
                min_index = i
        #After finding the smallest element in the array and its index, append it to the new array
        #and remove the element from the original array
        sorted_lst.append(min_elem)
        
        aLst.pop(min_index)
       
    return sorted_lst


def main():
    #Test case
    print(sort_function([10,9,8,7,6,5]))

    #Test case
    print(sort_function([100,-10,20,4,-99,54]))
           
main()
