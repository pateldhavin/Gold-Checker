import time
import requests

API_KEY = "52NRB0LRUJKKF8OP"  #API Key generated from my account

#Function that recives prices from Alphavantage API
def retrieve_price():
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=XAUUSD&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract the current price from the API response
    price = float(data["Global Quote"]["05. price"])
    return price

#Functions that writes prices to text file
#Converts the JSON results into a txt format
def track_price_changes():
    output_file = open("price_changes.txt", "a")  # Open file in append mode

    while True:
        try:
            price = retrieve_price()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S") # Formats the timestamp
            output_file.write(f"{timestamp} - Price: {price} USD\n")  # Write timestamp and price to file
            output_file.flush()  # Ensures that the data is immediatly written to file
            print(f"{timestamp} - Price: {price}")  # Print the current price


        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(86400)  # Wait for 24 hours before retrieving the price again

    output_file.close()  # Close the file when finished

track_price_changes()
