def review(rating):
    if rating<0:
        raise Exception("too low")
    else:
        print("done!")
try:
    review(-2)
except Exception as e:
    print(e)
print("hello")
print("stop")



# def poll(age):
#     if age<18:
#         raise Exception as e:
#         print(e)