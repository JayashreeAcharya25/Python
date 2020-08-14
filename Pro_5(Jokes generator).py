import pyjokes
n = int(input("How many Jokes:"))

for i in range(1,n):
 print(i,pyjokes.get_joke())