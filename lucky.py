#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4
print('Googling...') # display text while downloading the Google page

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
print(res.raise_for_status())
print(res)


# TODO: Retrieve top search result links.s
# print(res.text)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
print(soup.select('a'))
# TODO: Open a browser tab for each result.
