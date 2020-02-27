class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在快乐地玩耍' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在看片' % self._name)
        else:
            print('%s只能看熊出没' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        # 继承
        super(Student, self).__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self.grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s课程' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super(Teacher, self).__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s' % (self._name, self._title, course))


def main():
    stu = Student('陈亚萌', 11, '初三')
    stu.study('数学')
    stu.watch_av()

    t = Teacher('杨永慧', 33, '专家')
    t.teach('python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()
