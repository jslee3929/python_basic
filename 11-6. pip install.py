# pip install

# pip install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list : 현재 설치된 패키지 리스트 보여줌

# pip show beautifulsoup4 : beautifulsoup4 정보 보여줌

# pip install --upgrade beautifulsoup4 : beautifulsoup4 업그레이드하기

# pip uninstall beaugifulsoup4 : beautifulsoup4 삭제