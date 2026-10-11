import urllib
import webbrowser
import urllib.request
ur=urllib.request.urlopen('https://www.google.com/')
a=ur.getcode()
b=ur.read()
c=ur.geturl()
if a==200:
	s="no redirect"
else:
	s="redirect may happen"
print(s)
#print(b)
print("loging in to",c)
q="who is einstein"
q=input('search here:')
w=q.split()
str="+".join(w)
t=input("google or youtube?")
print(f"searching {str} in {t}")
webbrowser.open(f"https://www.{t}.com/search?q={str}&oq={str}")

