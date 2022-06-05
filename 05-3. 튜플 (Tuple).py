# 튜플
# 구성 요소의 변경이 불가능.
# 속도가 리스트보다 빠름.

menu = ("돈까스", "치즈까스") # 튜플은 ()를 쓴다.
print(menu[0])
print(menu[1])

# 아래처럼 할 수 없다. list와 차이점.
# menu.add("생선까스")
# menu.append("생선까스")

# 따로따로 선언할 수 있지만
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 모아서 선언할 수도 있다!
name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)

# 튜플 선언할 때 괄호는 써도 되고 안 써도 됨.
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)