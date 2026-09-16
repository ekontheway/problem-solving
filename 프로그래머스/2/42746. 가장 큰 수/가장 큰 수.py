def solution(numbers):
    str_nums = sorted([str(n) for n in numbers], key = lambda x : x*3, reverse=True)
    
    if(str_nums[0] == '0'):
        return '0'
    
    return ''.join(str_nums)