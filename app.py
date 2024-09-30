from flask import Flask, render_template  # Import Flask and template rendering
import random  # Import random module to randomly pick a quote

# Step 1: Create a Flask web application
app = Flask(__name__)

# Step 2: Define a function that reads the quotes file and returns a random quote
def get_random_quote():
    # Open the 'quotes.txt' file to read the quotes
    with open('src/quotes.txt', 'r') as file:
        quotes = file.readlines()  # Read all the lines (quotes) into a list

    # Clean up the quotes: remove empty lines and strip spaces/newlines
    quotes = [quote.strip() for quote in quotes if quote.strip()]

    # Return one random quote from the list
    return random.choice(quotes)

# Step 3: Create a route that listens for people visiting the website
@app.route('/')
def home():
    # Get a random quote using the function we defined above
    random_quote = get_random_quote()
    
    # Render the 'quote.html' template and pass the random quote to it
    return render_template('quote.html', quote=random_quote)

# Step 4: Run the web application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app in debug mode so we can see errors if they happen
