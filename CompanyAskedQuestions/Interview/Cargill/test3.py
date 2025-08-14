class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        # self.teachers =[]
        # self.students =[]
        # self.classrooms =[]
        # self.schedule =[]

class Classroom:
    def __init__(self,class_id, name):
        self.class_id = class_id
        self.name = name
        
class Subject:
    def __init__(self,subject_name, subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code

class Teacher:
    def __init__(self,teacher_id, teacher_name,list_of_subject):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.subjects = list_of_subject
class Student:
    def __init__(self,student_id,student_name,class_id,list_of_subjects):
        self.student_id = student_id
        self.student_name = student_name
        self.class_id = class_id
        self.subjects = list_of_subjects
        
class Scheduler:
    def __init__(self,schedule_id,teacher,class_id,subject,start_time, end_time):
        self.schedule_id = schedule_id
        self.teacher = teacher
        self.class_id = class_id
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time