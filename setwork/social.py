# users=["rahul","rohit","kohili","rishab","sanju","pandya","siraj"]
# rahul_followers=["rohit","kohili","rishab","rahul"]

# rahul_follow_suggestion=set(users).difference(set(rahul_followers))
# print(rahul_follow_suggestion)

users=["rahul","rohit","kohili","rishab","sanju","pandya","siraj"]
rahul_followers=["rohit","kohili","rishab","rahul"]
sanju_followers=["sanju","rohit","kohili"]
mutal_friends=set(rahul_followers).intersection(set(sanju_followers))
print(mutal_friends)