def solution(lottos, win_nums):
    match = (6, 6, 5, 4, 3, 2, 1)

    zeros = 6 - len(set(lottos) - {0})
    inter = len(set(win_nums) & set(lottos))
    max_ = inter + zeros
    min_ = inter

    return [match[max_], match[min_]]

"""
[44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]	[1, 1]
"""
lottos, win_nums = [45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))