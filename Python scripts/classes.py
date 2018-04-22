class Subject:
    sub_name = 'Social'
    sub_code = '11L102'
    sub_weightage = 3
    def display(self, stu_class,stu_roll_no,stu_name):
      # print ('hi',class_name)
        print ( 'subject',self.sub_name,'SubjectCode',self.sub_code,'SubjectWeightage',self.sub_weightage,'StudentClass',stu_class,'StdentRollnum',stu_roll_no,'StudentName',stu_name)

class Student(Subject):
    stu_class = 'V'
    stu_roll_no = 12
    stu_name = "David"

student = Student()

student.display(student.stu_class, student.stu_roll_no, student.stu_name)