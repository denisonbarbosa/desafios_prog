class Student:
    def __init__(self, id, relations=[]):
        self.id = id
        self.relations = relations
    

def separated_rooms():
    while True:
        n_students = input()
        
        if n_students == 0:
            break
        
        student_list = []
        for _ in range(n_students):
            student_id = input()
            student_relation = list(map(int, input().split()))
            student_list.append(Student(student_id, student_relation))
            

        

if __name__ == '__main__':
    separated_rooms()