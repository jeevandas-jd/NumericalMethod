
def BinarySearch(nums,key):

    low,high=0,len(nums)-1

    while low<high:
        mid=(low+high-1)//2

        if nums[mid]==key:

            return mid
        elif nums[mid]<high:
            low=mid
        else:
            high=mid
    
    return -1



l=[1,2,3,4,5,6,7]

print(BinarySearch(l,2))