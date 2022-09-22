def solution(nums):
    n = len(nums)
    po_info = []
    for i in nums:
        if i not in po_info:
            po_info.append(i)
    if len(po_info) >= n//2:
        answer = n//2
    else:
        answer = len(po_info)
    return answer

