import flask
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
quotes = [
    {'id': 0,
     'first_name': 'Maxine',
     'last_name': 'Hong Kingston',
     'quote': 'I learned to make my mind large, as the universe is large, so that there is room for paradoxes.',
     'type': 'inspirational',
     'note': 'From Woman Warrior'},
    {'id': 1,
     'first_name': ' Arundhati',
     'last_name':'Roy',
     'quote': 'Our strategy should be not only to confront empire, but to lay siege to it. To deprive it of oxygen. To shame it. To mock it. With our art, our music, our literature, our stubbornness, our joy, our brilliance, our sheer relentlessness – and our ability to tell our own stories. Stories that are different from the ones we’re being brainwashed to believe.',
     'type': 'rebellion',
     'note': ''},
    {'id': 2,
     'first_name': 'Bruce',
     'last_name': 'Lee',
     'quote': 'Empty your mind, be formless. Shapeless, like water.',
     'type': 'meditation',
     'note': ''}
]


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')


@app.route('/api/v1/resources/quotes/all', methods=['GET'])
def api_all():
    return jsonify(quotes)


@app.route('/api/v1/resources/quotes', methods=['GET'])
def filter_api():
    # Create an empty list for our results
    # Check if a parameter was provided as part of the URL.
    # If parameter is provided, assign it to a variable.
    # Loop through the data and match results that fit the requested parameter.
    # If no ID is provided, display an error in the browser.
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    results = []
    
    for i in request.args:
        if i == 'id':
            id = int(request.args['id'])
            for quote in quotes:
                if quote['id'] == id:
                    results.append(quote)
        
        elif i == 'first_name':
            first_name = request.args['first_name']
            for quote in quotes:
                if quote['first_name'].lower() == first_name.lower():
                    results.append(quote)
        else:
            return "Error: The field was not provided. Please specify an valid field in the query parameters."

    return jsonify(results)




app.run()
