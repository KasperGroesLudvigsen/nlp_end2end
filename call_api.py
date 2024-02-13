import requests

# Set the URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/analyze"


messages = ["This tutorial is very useful", "I did not sleep well so I am grumpy"]


for message in messages:

    # Define the input data as a dictionary
    data = {"input_string": message}


    # Check if the request was successful (status code 200)
    try:
        
        # Make a POST request to the endpoint
        response = requests.post(url, json=data)
        
        # Print the response from the server
        print(f"The sentiment is {response.json()["result"]["sentiment"]} with a score of {round(response.json()["result"]["score"], 3)}")

    except Exception as err:

        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {err}")
