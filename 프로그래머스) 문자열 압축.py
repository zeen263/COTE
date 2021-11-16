import sys


def solution(s):
    LEN = len(s)
    zipped = ["" for _ in range(LEN+1)]

    if LEN==1:
        return 1

    for window in range(1, LEN // 2 +1):
        cnt = 1
        old = s[0:window]

        for i in range(window, LEN+1, window):  # window개 단위로 문자열을 쪼갠다
            new = s[i:i+window]

            if old == new:  # 같으면 압축
                cnt += 1

            else:  # 다르면 누적된 압축물을 업데이트하고 새거 보기 시작
                if cnt == 1:  # 1은 생략 가능
                    zipped[window] += old
                else:
                    zipped[window] += (str(cnt) + old)

                if len(old) != len(new):  # 딱 안 떨어지고 남는 거
                    zipped[window] += new

                cnt = 1

            old = new

    result = [len(x) for x in zipped if x!=""]
    return min(result)




"""
"aabbaccc"  7
"ababcdcdababcdcd" 9
"abcabcdede" 8
"abcabcabcabcdededededede" 14
"xababcdcdababcdcd" 17
"""

s = "xs"
print(solution(s))
