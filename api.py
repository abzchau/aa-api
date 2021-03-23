import flask
from flask import request, jsonify, render_template
import random
import jinja2 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create a list of dicts for the data.
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
     'note': ''},
    {'id': 3,
     'first_name': 'Edward',
     'last_name': 'Said',
     'quote': 'It isn’t at all a matter of being optimistic, but rather of continuing to have faith in the ongoing and literally unending process of emancipation and enlightenment that, in my opinion, frames and gives direction to the intellectual vocation.',
     'type': 'rebellion',
     'note': 'Preface to Orientalism'},
    {'id': 4,
     'first_name': 'I.M.',
     'last_name': 'Pei',
     'quote': 'Stop worrying about missed opportunities and start looking for new ones.',
     'type': 'inspirational',
     'note': ''}
]


@app.route('/', methods=['GET'])
def home():
    quote = random.choice(quotes)
    random_quote = quote['quote']
    return render_template('homepage.html', random_quote=random_quote)


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

        elif i == 'last_name':
            last_name = request.args['last_name']
            for quote in quotes:
                if quote['last_name'].lower() == last_name.lower():
                    results.append(quote)

        elif i == 'type':
            type = request.args['type']
            for quote in quotes:
                if quote['type'].lower() == type.lower():
                    results.append(quote)
        else:
            return "Error: The field was not provided. Please specify an valid field in the query parameters."

    return jsonify(results)




app.run()
