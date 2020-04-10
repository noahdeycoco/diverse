import webbrowser
import requests
import bs4
# webbrowser.open('http://inventwithpython.com/')

# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# print(type(res))


# print(res.status_code)
# print(requests.codes.ok)
# print(res.raise_for_status())

# try:
#     res.raise_for_status() 
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

example = """
<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http:// inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
"""


# soup = bs4.BeautifulSoup(example, features="html.parser")
# print(soup)
# print(type(soup))

# print(soup.select('div'))
# print(soup.select('strong'))
# print(soup.select('.notice'))
# print(soup.select('div > span'))
# print(soup.select('input[type="button"]'))
# print(soup.select('#author'))
# print(soup.select('div span'))
# print(soup.select('input[name]'))

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.7146&lon=-74.0071#.XozEgC3pM_U')

soup2 = bs4.BeautifulSoup(res.text, features="html.parser")

print(soup2.select("p.myforecast-current-lrg")[0].getText())
