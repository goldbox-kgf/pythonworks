f1=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\all_students.txt","r")
f2=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\failed.txt","r")
all_student_set=set()
failed_students_set=set()
for line in f1:
    line=line.rstrip("\n")
    all_student_set.add(line)
for line in f2:
    line=line.rstrip("\n")
    failed_students_set.add(line) 
passed_students=all_student_set.difference(failed_students_set)
print(passed_students)       