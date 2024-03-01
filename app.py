from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def soupscrape(htmlID, htmlclass, URL):
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        foundscraped = soup.find(htmlclass, id=htmlID).text
        return foundscraped
    except Exception as e:
        print("Error:", e)
        return 'Error occurred'

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


