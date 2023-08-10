# Abitary argument are define by  *args


def user_f(*args):
    for i in args:
        print(i)
    print(args)

print('------------------------------------------------------------')
print(' Abitary argument are define by  *args')
print('---------------------------------------------------------------')
user_f('SAMUEL EFFIONG JACOB', 22,"Fulltime,fullstack,DevOps", 100.357)

print('-------------------------------------------------------------------------')


# Method of class Attributes
class Student():
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_tracks(self):
        return self.tracks

    def get_score(self):
        return self.score
    


students = Student("SAMUEL EFFIONG JACOB", 22,
                   "Fulltime,fullstack,DevOps", 100.357)

print('Structured Student Attributes Specified')
print('----------------------------')
print("I am by Name :" + students.get_name())
print('----------------------------')
print("Am Currently :" "",students.get_age())
print('----------------------------')
print("My Track,Course in Zuri :" + students.get_tracks())
print('----------------------------')
print("My Score So Far in Zuri :" "",students.get_score())
print('-----------------------------------------')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!! END OF Student Attributes Specified !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('---------------------------------------------------------------------')

##   methods for class “Student”:
class Student_change():
    def __init__(self, change_name, change_age, add_track, get_score):
          self.change_name = change_name
          self.change_age = change_age
          self.add_track = add_track
          self.get_score = get_score

    def get_change_name(self):
        return self.change_name

    def get_change_age(self):
        return self.change_age

    def get_add_track(self):
        return self.add_track

    def get_get_score(self):
        return self.get_score

sam = Student_change(change_name="Bob", change_age=26, add_track=["FE", "BE"], get_score=20.90)
Bob = sam=Student_change("Peter",34,"UI/UX",856.44)
## Result of methods output
print('Qustion 3: methods for class')
print('-----------------------------------------')
print('Give the Below Information to change their Atribute with Specifications Of Display Result')
print('---------------------------------------------------------------------------')
print('Bob = Student_change(change_name="Bob", change_age=26, add_track=["FE", "BE"], get_score=20.90)')
print('-----------------------------------------')
print("Name Change :" + Bob.get_change_name())
print('-----------------------------------------')
print("Age Change :" "", Bob.get_change_age())
print('-----------------------------------------')
print("Track Change :" + Bob.get_add_track())
print('-----------------------------------------')
print("Score Change :" "" , Bob.get_get_score())
print('-----------------------------------------')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!! END Qustion 3: methods for class !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

## Original work
# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
