from googlesearch import search
query = "Python"

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)