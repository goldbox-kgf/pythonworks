years_path="C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\years_write.txt"
leap_path="C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\leap_year_write.txt"
centuary_path="C:\\Users\\Personal\\OneDrive\\Desktop\\pythonprgms\\file data sets\\centuary_year_write.txt"

f_read=open(years_path,"r")
f_centuary=open(centuary_path,"w")
f_leap=open(leap_path,"w")

for year in f_read:
    year=int(year)
    if year%100==0:
        f_centuary.write(str(year)+"\n")
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        f_leap.write(str(year)+"\n")


f_read.close()
f_centuary.close()
f_leap.close()            