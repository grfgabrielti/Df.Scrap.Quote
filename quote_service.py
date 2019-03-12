from flask import Flask
import json
import spider_google_quote


app = Flask(__name__)

@app.route('/quote/<quote>', methods=['GET'])
def home(quote):
    result = spider_google_quote.get_price_of_quote(quote)
    result = result.replace(',','.')
    data = {}
    data['quote'] = quote
    data['value'] = result
    json_data = json.dumps(data)
    return json_data, 200

app.run(port=5001)
