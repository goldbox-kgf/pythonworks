f=open("C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\years_write.txt","w")
for year in range(1800,2025):
    f.write(str(year)+"\n")
f.close()    