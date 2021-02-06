class Person:
    def __init__(self, param_name):  #  self = 인자에 자기 자신을 넘겨주는 것. 콜문에 인자를 안 남겨도 파이썬이 알아서 넘겨준다.
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print(f"안녕하세요, 제 이름은 {self.name}입니다.")

person1 = Person("유재석")     # Person() -> 생성자(객체를 생성할 때 쓰는 함수)
person1.talk()
person2 = Person("박명수")
person2.talk()
