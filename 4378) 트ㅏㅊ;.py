"""
EOF 문제
input()은 EOF 에러를 발생시키기 때문에 try/except을 써서 EOF를 파악할 수 있다
(EOF까지 읽고 더 읽을 게 없을 때 종료해야 할 경우 유용함)

sys.stdin.readline()은 EOF에서 빈 문자열을 생성하기 때문에 입력 초과가 발생한다!
속도 때문에 input을 못 쓰면 sys.stdin.read()를 사용한다.
"""

typo = dict()

typo['1'] = '`'
typo['2'] = '1'
typo['3'] = '2'
typo['4'] = '3'
typo['5'] = '4'
typo['6'] = '5'
typo['7'] = '6'
typo['8'] = '7'
typo['9'] = '8'
typo['0'] = '9'
typo['-'] = '0'
typo['='] = '-'

typo['W'] = 'Q'
typo['E'] = 'W'
typo['R'] = 'E'
typo['T'] = 'R'
typo['Y'] = 'T'
typo['U'] = 'Y'
typo['I'] = 'U'
typo['O'] = 'I'
typo['P'] = 'O'
typo['['] = 'P'
typo[']'] = '['
typo['\\'] = ']'

typo['S'] = 'A'
typo['D'] = 'S'
typo['F'] = 'D'
typo['G'] = 'F'
typo['H'] = 'G'
typo['J'] = 'H'
typo['K'] = 'J'
typo['L'] = 'K'
typo[';'] = 'L'
typo["'"] = ';'

typo['X'] = 'Z'
typo['C'] = 'X'
typo['V'] = 'C'
typo['B'] = 'V'
typo['N'] = 'B'
typo['M'] = 'N'
typo[','] = 'M'
typo['.'] = ','
typo['/'] = '.'

typo[' '] = ' '
typo['\n'] = ''

'''
lines = sys.stdin.readlines()  # 이렇게 하면 데이터를 다 읽고 결과를 퉤퉤 한번에 뱉어내나봐
for line in lines:
    for ch in line.strip():
        print(typo[ch], end='')
    print()
'''

while True:
    try:
        for ch in input():  # 이렇게 하면 데이터 하나 읽고 결과 하나 뱉고 하는 듯?
            print(typo[ch], end='')
        print()
    except:
        break
