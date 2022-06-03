class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        # self.change_name = change_name
        # self.change_age = change_age
        # self.add_track = add_track
        # self.get_score = get_score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.tracks = tracks

    def get_score(self, score=30):
        self.score = score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)