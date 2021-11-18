def binary_search(lisst,target,lower_range=None,upper_range=None):
    length_of_list=len(lisst)
    if lower_range==None:
        lower_range=0
    if upper_range== None:
        upper_range=length_of_list-1

    mid_point=(lower_range+upper_range)//2
    
    if lower_range>upper_range:
        return -1 

    if target==lisst[mid_point]:
        return mid_point
    if target<lisst[mid_point]:
        return binary_search(lisst,target,lower_range,mid_point-1)
    if target>lisst[mid_point]:
        return binary_search(lisst,target,mid_point+1,upper_range) 


if __name__=="__main__":
    list_to_searched=[1,2,3,4,5,6,0,8]
    list_to_searched.sort() 
    # or list_to_be_searched=sorted(list_to_be_searched)
    target=int(input('enter the target number'))
    print(binary_search(list_to_searched,target))
    sorted()