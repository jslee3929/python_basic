# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

# 예) 생성된 비밀번호 : nav51!

# 내 풀이
# url = input('URL을 입력하세요 : ') # URL 입력 ex) http://naver.com
# url = url.replace('http://', '') # 'http://'를 지움. ex) naver.com
# url = url.replace(url[url.index('.'):], '') # '.' 뒤부터 끝까지 지움. ex) naver

# num1 = len(url) # 남은 URL의 길이를 셈. ex) 5
# num2 = url.count('e') # URL에 들어있는 'e'의 갯수를 셈. ex) 1

# url = url[0:3] # URL의 첫 세글자만 남기고 자름. ex) nav

# print('생성된 비밀번호 : {0}{1}{2}!'.format(url, num1, num2)) # 비밀번호 생성. nav51!

# 쌤 풀이
# url = "http://naver.com"
# my_str = url.replace("http://","") # 'http://'를 지움. naver.com
# my_str = my_str[:my_str.index(".")] # 처음부터 '.' 전까지만 남김.
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!' # password 변수에 비밀번호 설정
# print('{0}의 비밀번호는 {1}입니다.'.format(url, password)) # 비밀번호 출력

# 내 풀이 #2
url = input('URL을 입력하세요 : ') # URL 입력 ex) http://naver.com
url = url.replace('http://', '') # 'http://'를 지움. ex) naver.com
url = url[:url.index('.')] # 처음부터 '.' 전까지만 남김. ex) naver

num1 = len(url) # 남은 URL의 길이를 셈. ex) 5
num2 = url.count('e') # URL에 들어있는 'e'의 갯수를 셈. ex) 1

url = url[0:3] # URL의 첫 세글자만 남기고 자름. ex) nav

print('생성된 비밀번호 : {0}{1}{2}!'.format(url, num1, num2)) # 비밀번호 생성. nav51!