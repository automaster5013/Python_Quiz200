# bit1 = 0x61; bit2 = 0x62
# print(hex(bit1 & bit2))         # 0x60이 출력됨
# print(hex(bit1 | bit2))         # 0x63이 출력됨
# print(hex(bit1 ^ bit2))         # 0x3이 출력됨
# print(hex(bit1 >> 1))           # 0x30이 출력됨
# print(hex(bit1 << 2))           # 0x184가 출력됨



byte1 = 0x6b

# 하위 4비트 추출
lower_4bit = byte1 & 0x0f

# 상위 4비트 추출
upper_4bit = (byte1 >> 4) & 0x0f

print(hex(lower_4bit))
print(hex(upper_4bit))



