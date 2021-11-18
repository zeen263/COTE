import math

def solution(numbers, hand):
    pad = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    pad_dict = dict()

    thumb = {'left':(3, 0), 'right':(3, 2)}
    LEFT = (1, 4, 7, '*')
    RIGHT = (3, 6, 9, '#')

    for i in range(4):
        for j in range(3):
            key = pad[i][j]
            pad_dict[key] = (i, j)

    answer = ""
    for num in numbers:
        key_pos = pad_dict[num]
        if num in LEFT:
            answer += "L"
            thumb['left'] = key_pos

        elif num in RIGHT:
            answer += "R"
            thumb['right'] = key_pos

        else:
            d_l = dist(key_pos, thumb['left'])
            d_r = dist(key_pos, thumb['right'])

            if d_l == d_r:
                answer += hand[0].upper()
                thumb[hand] = key_pos

            elif d_l < d_r:
                answer += "L"
                thumb['left'] = key_pos

            elif d_l > d_r:
                answer += "R"
                thumb['right'] = key_pos

    return answer


def dist(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1]-v2[1])

numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
print(solution(numbers, hand))