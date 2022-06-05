# 외장 함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir 명령과 동일)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 검색

# os : 운영체제에서 제공하는 기본 기능
# ex) 폴더 만들기, 폴더 삭제
import os
print(os.getcwd()) # 현재 디렉토리 표시

folder = 'sample_dir'

if os.path.exists(folder):
    print('이미 존재하는 폴더입니다.')
    os.rmdir(folder)
    print(folder, '폴더를 삭제하였습니다.')
else:
    os.makedirs(folder) # sample.dir 폴더 생성
    print(folder, '폴더를 생성하였습니다.')

print(os.listdir()) # 현재 폴더 내 요소 표시

# time은 시간 관련 함수들을 제공하는 외장 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 년-월-일 시:분:초 형식으로 표시

# datetime
import datetime
print('오늘 날짜는', datetime.date.today(), '입니다.')

# timedate : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days = 100) # 100일 저장
print('우리가 만난지 100일은', today + td) # 오늘부터 100일 후