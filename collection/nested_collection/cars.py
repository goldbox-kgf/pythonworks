cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]
# total number of cars
# print(f"total number of cars: {len(cars)}")

# print available colorsof baleno
available_colours_of_baleno=[c.get("colors") for c in cars if c.get("name")=="baleno"]
# print(available_colours_of_baleno[0])

# print all brands

all_brands=[c.get("brand") for c in cars]
# print(set(all_brands))

# print car names available in amt transmissions
# amt_car=[c.get("name") for c in cars if "amt" in c.get("tranmissions")]
# print(amt_car)

# cars available in blue colors
blue_colored_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]
# print(blue_colored_cars)

# print all types of transmission 

tranmission_types=[ t for c in cars for t in c.get("transmissions") ]
# print(set(tranmission_types))

# all colors
all_colors={color for c in cars for color in c.get("colors")}
# print(all_colors)

# print most popular color

# costly car
costly_car=max(cars,key=lambda d:d.get("price"))
# print(costly_car.get("name"))
 
# lowest priced car 
low_priced_car=min(cars,key=lambda d:d.get("price"))
# print(low_priced_car.get("name"))

# sorted cars
sorted_cars=sorted(cars,key=lambda d:d.get("price"),reverse=True)
sorted_car_names={c.get("name"):[c.get("price"),c.get("brand")]for c in sorted_cars}
print(sorted_car_names)