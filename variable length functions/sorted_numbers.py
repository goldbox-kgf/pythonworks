
def sorted(*args,**kwargs):
    if kwargs.get("reverse")=="True":
        return sorted(args,reverse=True)
    if kwargs.get("reverse")=="False":
        return sorted(args)
        

print(sorted(10,20,40,70,90,30,reverse="True")) 