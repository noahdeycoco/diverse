# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4

url = 'https://xkcd.com/' # starting url 
os.makedirs('data/xkcd', exist_ok=True) # store comics in ./xkcd 

# while not url.endswith('#'):
# # TODO: Download the page.
#     res = requests.get(url)
#     print(res)
# TODO: Find the URL of the comic image. 
# TODO: Download the image.
# TODO: Save the image to ./xkcd.
# TODO: Get the Prev button's url.

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
# links = soup.find_all(id = 'comic')

comicElem = soup.select('#comic img') 
if comicElem == []:
    print('Could not find comic image.') 
else:
    comicUrl = comicElem[0].get('src')
    # Download the image.s
    print('Downloading image %s...' % (comicUrl)) 
    res = requests.get('https:'+comicUrl) 
    res.raise_for_status()

 # Save the image to ./xkcd.
imageFile = open(os.path.join('data/xkcd', os.path.basename(comicUrl)), 'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)

imageFile.close()

# Get the Prev button's url.
prevLink = soup.select('a[rel="prev"]')[0]
url = 'http://xkcd.com' + prevLink.get('href')
print(url)
print('Done.')