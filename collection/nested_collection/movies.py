movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},
]

# print(len(movies))

movie_title=[m.get("title") for m in movies]

# print(movie_title)

malayalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]

# print("malayalam movies are:",malayalam_movies)

max_runTime=max(movies,key=lambda m:m.get("run_time"))

runTime=max_runTime.get("run_time")

name=[m.get("title") for m in movies if m.get("run_time")==runTime]

# print("highest_runTime movies are:",name)

# print(min(movies,key=lambda m:m.get("run_time")))

min_runTime=min(movies,key=lambda m:m.get("run_time"))

runtime=min_runTime.get("run_time")

name1=[m.get("title") for m in movies if m.get("run_time")==runtime]

# print("lowest_runtime",name1)

movie_in_2024=[m.get("title") for m in movies if m.get("year")==2024]

# print("2024 movies:",movie_in_2024)