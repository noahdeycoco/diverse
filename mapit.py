# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser
import sys

if len(sys.argv) > 1:
 # Get address from command line.
 address = ' '.join(sys.argv[1:]).replace(' ','+')
 

url = 'https://www.google.com/maps/place/'+address

webbrowser.open(url)
# print(address)
