import pyshorteners

s = pyshorteners.Shortener()

print(s.tinyurl.short('https://www.instagram.com/'))