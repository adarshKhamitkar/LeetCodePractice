def find_intervals(n:int, nums:list[int], target_sum:int):
    """
    :type input: Dict[str, Any]
    :rtype: List[List[int]]
    """
    
    res= []
    n_len = len(nums)
    _sum, l = 0, 0
    for r in range(n_len):
        _sum += nums[r]
        
        while _sum > target_sum:
            _sum -= nums[l]
            l+=1
        
        if _sum == target_sum:
            res.append(nums[l:r+1])
        if len(res) == n:
            break

    res.sort(key=lambda x: len(x))
        
    return res


print(find_intervals(2, [1,2,3,4,5], 5))