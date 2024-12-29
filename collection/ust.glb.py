arr=[100,800,300,600,500,600,700,200]
odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0]
odd_position_elements.reverse

print(odd_position_elements)
