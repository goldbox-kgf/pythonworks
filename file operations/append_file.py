f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\frameworks.txt","a")
frame_works=["wordpress","springboot","oodo","fastapi"]
for fw in frame_works:
    f.write(fw+"\n")
f.close()