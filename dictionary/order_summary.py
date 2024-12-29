orders=["chaya","kappi","chaya","kappi","ghee roast","plain roast","poratta","chaya"]
order_summary={}
for w in orders:
    if w in order_summary:
        order_summary[w]+=1
    else:
        order_summary[w]=1
print(order_summary)            