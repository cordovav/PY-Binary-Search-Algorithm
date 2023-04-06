# code your iterative algorithm here
def binary_search(data, el):
    #crewting a function that takes in list and elements
    #create 2 variables to store index values first and last
    first = 0
    last = len(data)-1
    #set found variable to False, True will be uesd if desired variable is found
    found = False

    #create a while loop that runs when first is less than or greater than last ans element is not found
    while first <= last and not found:
        #asign variable mid that will store the middle elements index by adding the first and last position 
        #together and diving by 2 but using // to return a whole integer and not a floating integer
        mid = (first+last)//2

        #now create a while loop tocheck if the middle element is equal to our desired element
        #if so set found to True
        if data[mid] == el:
            found = True
            
            #lets decide what half to use
            #if the desired element is < mid element value, set last = to one less than the middle element(mid-1)
        else:
            if el < data[mid]:
                last = mid - 1
                #else we deal with the right half, set first - to one more than the index of middle (mid+1)
            else:
                first = mid + 1

    #finally return your vafiable
    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(binary_search(test_list, 10))   