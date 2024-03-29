
from flask import jsonify
import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/John_von_Neumann'

response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')

# Find the specific data you want to extract from the page
# For example, to extract the title of the page:

# https://en.wikipedia.org/wiki/Stoneleigh_Abbey_Gatehouse?wprov=sfti1#

htmlclassExample = 'h1'

htmlIDexample = 'firstHeading'

def soupscrape(htmlID, htmlclass, URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        pulled = soup.find(htmlclass, htmlID)
        foundscraped = pulled
        return(foundscraped)
    except:
        return('errorz')


#htmlid = input("htmlID")

#htmlclass = input("htmlclass")

#url = input("URL")

#print(soupscrape(htmlid, htmlclass, url))

#print(jsonify(soupscrape(htmlid, htmlclass, url)))