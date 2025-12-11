def merge_sorted_arrays(arr1, arr2):
    """ 
    :type input: Tuple[List[int], List[int]]
    :rtype: List[int] 
    """
    res = []
    l,r = 0,0
    m,n = len(arr1), len(arr2)
    
    while l<m and r<n:
        if arr1[l] < arr2[r]:
            res.append(arr1[l])
            l+=1
        else:
            res.append(arr2[r])
            r+=1
            
    if l < m and r == n:
        res.extend(arr1[l:(m+1)])
    elif r < n and l == m:
        res.extend(arr2[r:(n+1)])
        
    return res
    

#print(merge_sorted_arrays([1,3,5,7], [2,4,6,8]))
print(merge_sorted_arrays([-10, 0, 3, 25], [-25, -5, 1, 14, 30]))

#Time Complexity: O(M + N)
#Space Complexity: O(M + N)