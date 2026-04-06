# while 조건:
#     조건이 참일 때 반복 실행 코드
#     ~
#     continue    # while문 처음으로 이동하여 반복 실행 코드 계속
#     ~
#     break   # while문 탈출

x = 0
while x < 0:
    x = x + 1
    if x < 3:
        continue

    print(x)
    if x > 4:
        break


n = 1
total = 0
while True:
    total = total + n
    if total > 100000:
        print('1+2+...+n 값이 10만보다 커지게 되는 n: ',n)
        print('이때 총합은', total)
        break
    n = n + 1

