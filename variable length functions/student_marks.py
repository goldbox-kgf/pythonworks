ambady=input("enter the operation:=")
def student(*args,**kwargs):
    if kwargs.get("operation")=="avg":
        return sum(args)/len(args)
    if kwargs.get("operation")=="total":
        return sum(args)
        

print(student(10,20,30,operation=ambady))        