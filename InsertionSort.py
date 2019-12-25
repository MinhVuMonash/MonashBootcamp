#Insertion Sort

def InsertionSort(L):
    listLength = len(L)
    for i in range(1,listLength):
        key = L[i]
        j = i -1
        while j >= 0 and key < L[j]:
            #swap
            L[j+1] =L[j]
            j -=1
        L[j+1] = key 

    return L



def main():
    numL = [2,4,1,-10,200,123,-90]
    print(InsertionSort(numL))



main()
