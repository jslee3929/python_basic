# 퀴즈 #13
# 데이터를 축약하여 인코딩하는 프로그램을 작성하시오
# (예시) aaabbbb = a3b4, ppqqqrrrs = p2q33r3s1

data = 'aaaaabbbccccddddddeeeeeeeee'
encoded = ''
count = 1

for i in range(1, len(data)):
    if data[i-1] == data[i]:
        count += 1
    else:
        encoded += data[i-1] + str(count)
        count = 1

    if i + 1 == len(data):
        encoded += data[i] + str(count)

print(encoded)