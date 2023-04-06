def recursive_bsearcch(lst, el):
    if len(lst) == 0:
        return False
    else:
        #define a variable(mid) and set equal to the index of the middle element
        #in this cae we want to find the length of the list and divide by 2
        mid = len(lst)//2

        #check if mid is equal to our desired element (el)
        if lst[mid] == el:
            return True
        else:
            #check if the desired value is < the (mid)
            if el < lst[mid]:
                #if so call the function again, but the first parameter will reptesent the adjusted list
                #this is done by index slicing to pass in the half of the list we want to recursively pass
                #for this case it will be the lower half of the elements in the arrat
                return recursive_bsearcch(lst[:mid], el)
            else:
                return recursive_bsearcch(lst[mid+1], el)
            

test_lst = [1,2,3,4,6,7,8,9]
print(recursive_bsearcch(test_lst, 2))