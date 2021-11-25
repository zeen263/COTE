from collections import defaultdict

def solution(record):
    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    user = defaultdict()

    res = []
    for query in record:

        status, uid, *name = query.split()

        if name:
            user[uid] = name[0]

        if status != "Change":
            res.append([uid, message[status]])

    ans = []
    for uid, msg in res:
        ans.append(user[uid] + msg)

    return ans


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

