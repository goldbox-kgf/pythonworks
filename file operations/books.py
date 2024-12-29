from json  import load
f=open("C:/Users/Personal/OneDrive/Desktop/pythonprgms/file data sets/books.json")
data=load(f)
# for books in data:
#     print(books)

all_titles=[book.get("title") for book in data]
# print(all_titles)

page_filter=[book.get("title") for book in data if book.get("pages")<250]
# print(page_filter)

genres=[book.get("genre") for book in data ]

# print(set(genres))

genre_count={genre:genres.count(genre)for genre in genres}
# print(genre_count)

costly_book=[book.get("title") for book in data if book.get("price")]
# print(max(costly_book))


all_authors=[book.get("author") for book in data]
# print(all_authors)
author_with_morethan_onebook={auth:all_authors.count(auth) for auth in all_authors}
print([k for k,v in author_with_morethan_onebook.items() if v>1])