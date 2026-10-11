#searching using wikipedia module  :-)
import wikipedia
# setting language to hindi
#wikipedia.set_lang("hi")
str=input("search here: ")
#search and display number of lines
result=wikipedia.summary(str,5)
print("finding your result")
print(result)
print()
#showing available topics on india
se=wikipedia.search(str)
print(se)
#infomatiormation about page 
page=wikipedia.page(str)
print()
print(page)
print(page.original_title)
print(page.links)

