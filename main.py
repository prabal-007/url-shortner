import pyshorteners

link = input('Enter link : ')
shortIt = pyshorteners.Shortener()

x = shortIt.tinyurl.short(link)
print(x)
