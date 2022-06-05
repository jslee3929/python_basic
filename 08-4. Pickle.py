# Pickle : 데이터를 파일로 저장 = 공유 가능!

# pickle에 내용 쓰기
import pickle
profile_file = open('profile.pickle', 'wb') # b = 바이너리. 피클은 항상 바이너리 타입을 정의해줘야 함.
profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 데이터를 profile_file에 저장.
profile_file.close()

# {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}

# pickle의 내용 읽기
profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file) # file에 있는 정보를 profile로 불러오기
print(profile)
profile_file.close()

# {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}