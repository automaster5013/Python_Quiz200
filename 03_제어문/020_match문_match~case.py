http_status = 400
match http_status:
    case 400:
        print('Bad Request')
    case 401:
        print('Unauthorized')
    case 402:
        print('Fobidden')
    case 403:
        print('Not found')
    case _:
        print('기타 인터넷 문제로 뭔가 잘못됨')


http_status = 302
match http_status:
    case 200|202|203:
        print('Success')
    case 301|302|303:
        print('Redirection')
    case 400|401|403|404:
        print('Client Errors')
    case _:
        print('기타 HTTP 응답 코드')


point = (0, 0)
# point = (1, 0)
# point = (0, 1)
# point = (1, 1)

match point:
    case (0, 0):
        print('원점 좌표')
    case (x, 0):
        print(f'x축 위의 점이며 x의 값은 {x}')
    case (0, y):
        print(f'y축 위의 점이며 y의 값은 {y}')
    case (x, y):
        print(f'(x, y) = ({x}, {y})')
    case _:
        print('오류: 2차원 좌표가 아님')


