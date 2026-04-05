# for 변수 in 범위:
#     반복적으로 실행할 코드

strData = 'abcdef'
for c in strData:
    print(c, end='-')


listData = [1, 2, 3, 4, 5]
for idx in listData:
    print(idx, end='-')


ascii_codes = {'a':97, 'b':98, 'c':99}
for code in ascii_codes.items():
    print(code)


for i in range(10):
    print(i, end='#')


# for 변수 in 범위:
#     ~ ~ ~
#     continue    # 다음 반복 실행.continue 아래 코드는 실행하지 않음
#     ~ ~ ~
#     break       # for문 탈출


for i in [1, 2, 3, 4, 5]:
    print(i)
    if i < 2:
        continue
    else:
        break


for i in [1, 2, 3, 4, 5]:
    print(i)
    if i == 2:
        break




