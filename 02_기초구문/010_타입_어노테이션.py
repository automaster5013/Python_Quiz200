name = '홍길동'
age = 17
weight = 70.7
is_badman = False

name: str = '홍길동'
age: int = 17
weight: float = 70.7
is_badman: bool = False

booklist: list[str] = ['삼국지', '수호지', '초한지']

island: tuple[str, float, float] = ('독도', 131.52, 37.14)

top4_familyname: dict[str, int] = {'김씨':123456, '나씨':345811, '박씨':963123, '이씨':865909}

fruits:set[str] = ['사과', '배', '수박', '참외', '딸기']

# print(__annotations__)
# {'name':<class 'str'>, 'age':<class 'int'>, 'weight':<class 'float'>, 
# 'is_badman':<class 'bool'>, 'booklist':str[str], 'island':tuple[str, float, float], 
# 'top4_singer':dict[str, int], 'fruits':set[str]}

fruits:set[str] = {'사과', '배', '수박', '참외', '딸기'}
fruits = {1, 2, 3, 4, 5}
print(fruits)




