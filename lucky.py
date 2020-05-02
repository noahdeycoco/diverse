#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, argparse, re, pprint
# print('Googling...') # display text while downloading the Google page

# res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://www.google.fr/search?q=capitaine+haddock')
# print(res.raise_for_status())
# print(res)

# file = open('data/google_search_capitaine_haddock.txt', 'w')
# file.write(res.text)
# file.close()

file = open('data/google_search_capitaine_haddock.txt', 'r')

# print(file.read())

# TODO: Retrieve top search result links
# print(res.text)
soup = bs4.BeautifulSoup(file.read(), features="html.parser")
# print(soup.select('a'))

# Open a browser tab for each result
linkElems = soup.select('.r a')
print(linkElems)
# print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print(linkElems[i].get('href'))

# TODO: Open a browser tab for each result.