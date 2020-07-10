class Student:
    def __init__(self,No,Name,Gender,Age):
        self.No=No
        self.Name=Name
        self.Gender=Gender
        self.Age=Age
    def show(self):
        print("%-16s %-16s %-8s %-4s" % (self.No, self.Name, self.Gender, self.Age))


class StudentList():
    def __init__(self):
        self.students = []
    def show(self):
        print("%-16s %-16s %-8s %-4s" % ("No", "Name", "Gender", "Age"))
        for s in self.students:
            s.show()
    def insert(self,s):
        i=0
        while i<len(self.students) and s.No>self.students[i].No:
            i=i+1
        if i<len(self.students) and s.No==self.students[i].No:
            print(s.No+" 已经存在")
            return False
        self.students.insert(i,s)
        print("增加成功")
        return True
    def update(self, s):
        flag = False
        for i in range(len(self.students)):
            if s.No == self.students[i].No:
                self.students[i].Name = s.Name
                self.students[i].Gender = s.Gender
                self.students[i].Age = s.Age
                print("修改成功")
                flag = True
                break
        if (not flag):
            print("没有这个学生")
        return flag
    def delete(self,No):
            flag=False
            for i in range(len(self.students)):
                if (self.students[i].No == No):
                    del self.students[i]
                    print("删除成功")
                    flag=True
                    break
            if (not flag):
                print("没有这个学生")
            return flag

n = StudentList()
while True:
    print(">" , end="")
    x = input()
    if x == "exit":
        break
    elif x == "show":
        n.show()
    elif x == "update":
        l = int(input("No="))
        o = input("Name=")
        i = input("Gender=")
        u = int(input("Age="))
        n.update(Student(l,o,i,u))
    elif x == "insert":
        l = int(input("No="))
        o = input("Name=")
        i = input("Gender=")
        u = int(input("Age="))
        n.insert(Student(l,o,i,u))
    elif x == "delete":
        l = int(input("No="))
        n.delete(l)