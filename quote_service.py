from flask import Flask
import spider_google_quote


app = Flask(__name__)

@app.route('/quote/<quote>', methods=['GET'])
def home(quote):
    result = spider_google_quote.get_price_of_quote(quote)
    result = result.replace(',','.')
    return result, 200

app.run(port=5001)
