arr=[10,20,30,40,2,3]
result={num:num**3 for num in arr}
# print(result)

# even_squares

arr=[10,20,30,40,2,3]
even_squares={num:num**2 for num in arr if num%2==0}
print("even:", even_squares)
# odd_cubes
odd_cubes={num:num**3 for num in arr if num%2!=0}
print("odd:",odd_cubes)










