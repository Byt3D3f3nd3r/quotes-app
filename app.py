import random  # Importing the random module to select a random line

# Open the quotes.txt file in read mode
with open('src/quotes.txt', 'r') as file:
    # Read all the lines from the file into a list
    quotes = file.readlines()

# Remove any empty lines and strip newline characters
quotes = [quote.strip() for quote in quotes if quote.strip()]

# Select a random quote from the list
random_quote = random.choice(quotes)

# Print the randomly selected quote
print("Here's a random movie quote for you:")

# Print the selected quote with line number
print(random_quote)
