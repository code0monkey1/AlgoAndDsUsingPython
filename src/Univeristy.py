
class Person():
    def __init__(self):
        self.name = None
        self.age = None
        self.title = None

    def setName(self):
        return input("Enter the persons name : ")

    def setAge(self):
        return int(input("Input the persons age :"))

    def introduceYourself(self):
        return f"Hi my name is {self.setName()} my age is {self.setAge()} and I am a {self.setTitle()} "

    def setTitle(self):
        return input("Enter the title of the person: ")


class UniversityPerson(Person):


    def introduceYourself(self):
        print(Person.introduceYourself(self) + f" and my operations are {self.defineYourOperations()}")


class Student(UniversityPerson):

    def defineYourOperations(self):
        mySubjects =[]

        while True:

            subject = input("Enter your subject , If the list of your subjects is finished , press $ ")

            if subject == "$":
                break
            else:
                mySubjects.append(subject)


        return "I study at the university and the list of my subjects mySubjects is :"+str(mySubjects)

    def introduceYourself(self):
        UniversityPerson.introduceYourself(self)


class Professor(UniversityPerson):
    def defineYourOperations(self):
        myClasses = set()

        while True:

            subject = input("Enter your classes , If the list of your classes is finished , press $ ")

            if subject == "$":
                break
            else:
                myClasses.add(subject)
        return str(myClasses)

    def introduceYourself(self):
        UniversityPerson.introduceYourself(self)

if __name__ == "__main__":
    student = Student()
    professor = Professor()

professor.introduceYourself()