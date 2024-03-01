

import urllib.request
import requests
from bs4 import BeautifulSoup

# Specify the URL of the Wikipedia page you want to scrape
url1 = 'https://en.wikipedia.org/wiki/web_scraping'
url = 'https://en.wikipedia.org/wiki/web_scraping'
# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the specific data you want to extract from the page
# For example, to extract the title of the page:

# https://en.wikipedia.org/wiki/Stoneleigh_Abbey_Gatehouse?wprov=sfti1#

htmlclass1 = 'h1'

htmlID = 'firstHeading'

def printsoup(htmlID, htmlclass, URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        title = soup.find(htmlclass, id=htmlID).text
        print("\n\n", title)
    except:
        print("\n an error has occured, probably missing id")

def questiontime():
    url = input("\n\nInput WIKI link:  ")
    url1 = 'https://en.wikipedia.org/wiki/web_scraping'

    htmlclass1 = input("HTML CLASS?  ")
    htmlID = input("htmlID?  ")

    response = requests.get(url)
    try:
        printsoup(htmlID, htmlclass1, url)
    except:
        print("an error has occured, in the printsoup html ID")


def storedlink():

    htmlclass1 = 'h1'
    htmlID = 'firstHeading'
    url1 = 'https://en.wikipedia.org/wiki/web_scraping'
    response = requests.get(url1)
    try:
        printsoup(htmlID, htmlclass1, url1)
    except:
        print("\nan error has occured, in the printsoup html ID")

def main():
    ans = input("\n\nselect mode\n\n(0 = codedlink)(1 = question)(2 = exit):  ")
    if ans == '0':
        try:
            storedlink()
        except:
            print("error in excecuting storedlink")
        main()
    elif ans == '1':
        try:
            questiontime()
        except:
            print("error in excecuting question time")
        main()
    elif ans == '2':
        exit()
    else:
        print("an error has occured try again")
        main()


main()
