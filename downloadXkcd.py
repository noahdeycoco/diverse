# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4

url = 'https://xkcd.com/' # starting url 
os.makedirs('data/xkcd', exist_ok=True) # store comics in ./xkcd 

# while not url.endswith('#'):
# # TODO: Download the page.
#     res = requests.get(url)
#     print(res)
# TODO: Find the URL of the comic image. # TODO: Download the image.
# TODO: Save the image to ./xkcd.
# TODO: Get the Prev button's url.

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
links = soup.find_all('a')

for i in links:
    print(i)
