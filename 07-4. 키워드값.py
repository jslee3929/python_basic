# 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

# 매개변수의 값을 키워드를 이용해 호출하면 순서가 섞여 있어도 잘 출력됨.
profile(name="유재석", age=20, main_lang="파이썬") # 유재석 20 파이썬
profile(age=25, main_lang="자바", name="김태호")   # 김태호 25 자바