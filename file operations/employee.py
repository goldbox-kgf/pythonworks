from json import load
f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\employee.json")
data=load(f)
for emp in data:
    print(emp)