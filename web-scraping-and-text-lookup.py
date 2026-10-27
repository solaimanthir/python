import requests
import bs4

#extract quotes from homepage
quotes = []
homepage = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(homepage.text, 'lxml')
quotes_list = soup.select('.text')
for q in quotes_list:
    quotes.append(q.text)
quotes

#find top ten tags
top_ten_tags = soup.select('.tag-item')
for item in top_ten_tags:
    print(item.text)

#find all authors from site
authors = set()
base_url = 'https://quotes.toscrape.com/page/{}/'
page=0

while True:
    page += 1
    url = 'https://quotes.toscrape.com/page/{}/'.format(page)
    htmltext = requests.get(url)
    soup = bs4.BeautifulSoup(htmltext.text, 'lxml')
    auts = soup.select('.author')

    #invalid page
    if len(auts) == 0:
        break
		
    #valid page
    for aut in auts:
        authors.add(aut.text)

authors

#find books with 3-star ratings
res_three_star_books = []

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

for i in range(1, 51):
    url = base_url.format(i)
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'lxml')
    prods = soup.select('.product_pod')

    for book in prods:
        if len(book.select('.star-rating.Three')) != 0:
            res_three_star_books.append(book.select('a')[1]['title'])

res_three_star_books

#Lookup a number in a directory recursively
import re
import os
def find(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    content = f.read()
    lookup = re.search(pattern, content)
    if lookup:
        return lookup
    else:
        return ''

results = []
for dir, sub_dirs, files in os.walk(os.getcwd()+'\\lookup_dir'):
    for f in files:
        full_path = dir+'\\'+f
        results.append(find(full_path))

for val in results:
    if val != '':
        print(val.group())
		
