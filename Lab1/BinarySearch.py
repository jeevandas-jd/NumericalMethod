
def BinarySearch(nums,key):

    low,high=0,len(nums)-1

    while low<high:
        mid=(low+high)//2

        if nums[mid]==key:

            return mid
        elif nums[mid]<key:
            low=mid
        else:
            high=mid-1
    
    return -1

if __name__=="__main__":
    n=int(input("enter number of elements"))

    l=[]

    for i in range(n):
        l.append(int(input("enter numbers/elements:>>>")))
    k=int(input("enter key/seach element:>>>"))
    a=BinarySearch(l,k)

    if a!=-1:
        print(f"key found at index {a}")
    else:
        print("sorry key not found in array")
