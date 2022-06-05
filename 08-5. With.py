# with
# with을 쓰면 close를 안 써도 됨.

import pickle

with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file))

# {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

with open('study.txt', 'w', encoding='utf8') as study_file:
    study_file.write('파이썬을 열심히 공부하고 있어요')

# 파이썬을 열심히 공부하고 있어요

with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())

# 파이썬을 열심히 공부하고 있어요