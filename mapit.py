import webbrowser
import requests

# webbrowser.open('http://inventwithpython.com/')


res = requests.get('https://www.loom.fr')
print(type(res))

print(res.text)


