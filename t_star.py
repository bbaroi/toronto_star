import bs4 as bs
import urllib.request
n=2
src=urllib.request.urlopen('https://www.thestar.com').read()
soup=bs.BeautifulSoup(src,'html.parser')

print("\n")
print("CHOOSE 1 OF THE TORONTO STAR NEWSPAPER SECTIONS TO READ THE HIGHLIGHTS")
print("-"*80)
print("\n")

print("*"*50)
print("NEWS SECTIONS:")
print("-"*20)
print("\n")
for i in soup.find_all('h1'):
    print("1",i.text)
for i in soup.find_all('h2'):
    a="Talking Points"
    if i.text not in a:
        print(n,i.text)
        n=n+1
print("*"*50)
print("\n")

while True:
    choose=input("Choose the section number to read the highlights[1-9]: ")
    if choose == "1":
        src=urllib.request.urlopen('https://www.thestar.com').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text)
    elif choose == "2":
        src=urllib.request.urlopen('https://www.thestar.com/news.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text)
    elif choose == "3":
        src=urllib.request.urlopen('https://www.thestar.com/opinion/star-columnists.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text) 
    elif choose == "4":
        src=urllib.request.urlopen('https://www.thestar.com/opinion.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text) 
    elif choose == "5":
        src=urllib.request.urlopen('https://www.thestar.com/news/gta.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text) 
    elif choose == "6":
        src=urllib.request.urlopen('https://www.thestar.com/sports.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text)
    elif choose == "7":
        src=urllib.request.urlopen('https://www.thestar.com/business.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text)
    elif choose == "8":
        src=urllib.request.urlopen('https://www.thestar.com/entertainment.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text)
    elif choose == "9":
        src=urllib.request.urlopen('https://www.thestar.com/life.html').read()
        soup=bs.BeautifulSoup(src,'html.parser')
        for i in soup.find_all('a'):
            print("\n",i.text)
    else:
        print("Choose a number between [1-9] to read from the sections highlights")
        pass
    cont=input("Would you like to read the highlights from another section?[yes or no]: ")
    if cont.lower() == "yes":
        pass
    else:
        break
 
