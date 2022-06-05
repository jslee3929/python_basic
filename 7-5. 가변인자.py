# 가변인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    # end=" "를 사용하면 print문이 끝날 때 줄바꿈 하지 않음.
    print(lang1, lang2, lang3, lang4, lang5)

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#')
# 이름 : 유재석   나이 : 20        Python Java C C++ C#

profile('김태호', 25, 'Kotlin', 'Swift', '', '', '')
# 이름 : 김태호   나이 : 25        Kotlin Swift

# 김태호에게 빈 값을 넣어주기 귀찮다.
# 혹은 유재석이 언어를 6개 이상 다룬다.
# 이럴 때 가변인자를 사용함.

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#', 'JavaScript')
# 이름 : 유재석   나이 : 20        Python Java C C++ C# JavaScript
profile('김태호', 25, 'Kotlin', 'Swift')
# 이름 : 김태호   나이 : 25        Kotlin Swift