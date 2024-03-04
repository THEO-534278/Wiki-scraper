
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from webscapingcode import *


app = Flask(__name__)

#def soupscrape(htmlID, htmlclass, URL):
#    try:
#        response = requests.get(URL)
#        soup = BeautifulSoup(response.content, 'html.parser')
#        foundscraped = soup.find(htmlclass, htmlID).text
#        return foundscraped
#    except Exception as e:
#        print("Error:", e)
#        return 'Error occurred'




def soupscrape1(htmlID, htmlclass, URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        foundscraped = soup.find(htmlclass, htmlID)
        return(foundscraped)
    except:
        return('errorz')



@app.route('/')
def main():
    return render_template('main.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data['url']
    scraped_data = soupscrape('firstHeader', 'h1', url)
    return jsonify(scraped_data)

if __name__ == '__main__':
    app.run(debug=True)


