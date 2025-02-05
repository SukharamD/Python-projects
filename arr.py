def find(arr,x,n):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1



if __name__=="__main__":
    arr = [1,2,3,4,5,6]
    n=len(arr)
    x = int(input(f"Enter a number between{arr} :"))

    res = find(arr,x,n)
    if res == -1:
        print("Number not present")
    else:
        print("number present at index ", res)

