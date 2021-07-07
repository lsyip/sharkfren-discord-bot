import requests


# Returns a random Bob Ross quote. 
def get_quote():
    "Retrieves Bob Ross quote from external API."
    response = requests.get("https://api.bobross.dev/api")
    json_response = response.json()

    quote = json_response['response'][0]['quote'] + " -Bob Ross"

    return quote