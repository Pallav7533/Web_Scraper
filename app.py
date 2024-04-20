from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        links = soup.find_all('a')
        return render_template('result.html', title=title, links=links)
    else:
        return "Error: Unable to fetch URL"

if __name__ == '__main__':
    app.run(debug=True)
