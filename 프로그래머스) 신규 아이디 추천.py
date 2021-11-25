from itertools import islice


def solution(new_id):
    for i in range(1, 8):
        new_id = eval('step' + str(i) + '(new_id)')
        print(i, new_id)

    return ''.join(new_id)


def step1(uid):
    return uid.lower()


def step2(uid):
    new_uid = []
    for ch in uid:
        if ch.isalpha() or ch.isdigit() or ch == '-' or ch == '_' or ch == '.':
            new_uid.append(ch)
    return new_uid


def step3(uid):
    new_uid = []
    LEN = len(uid)

    ch_ = uid[0]
    if ch_ != '.':
        new_uid.append(ch_)
    for ch in islice(uid, 1, None):
        if ch == '.' and ch == ch_:
            continue

        new_uid.append(ch)
        ch_ = ch

    return new_uid


def step4(uid):
    if uid and uid[0] == '.':
        uid = uid[1:]

    if uid and uid[-1] == '.':
        uid = uid[:-1]

    return uid


def step5(uid):
    if not uid:
        uid = 'a'

    return uid


def step6(uid):
    LEN = len(uid)
    if LEN > 15:
        uid = uid[:15]

    if uid[-1] == '.':
        uid = uid[:-1]

    return uid


def step7(uid):
    LEN = len(uid)
    if LEN < 3:
        uid += (uid[-1] * (3 - LEN))

    return uid


"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
"z-+.^."	                    "z--"
"=.="	                        "aaa"
"123_.def"	                    "123_.def"
"abcdefghijklmn.p"              "abcdefghijklmn"

uid = "...!@BaT#*..y.abcdefghijklm"
print(solution(uid))