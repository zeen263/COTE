def solution(n):
    ans = ""
    div, mod = divmod(n, 3)

    if mod == 0:
        div = max(div-1, 0)
        ans += "4"

    else:
        ans += str(mod)

    while div:
        div, mod = divmod(div, 3)

        if mod == 0:
            div = max(div-1, 0)
            ans += "4"

        else:
            ans += str(mod)

    return ans[::-1]

n = 11
print(solution(n))