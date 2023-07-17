import random
import requests

url = "https://icanhazdadjoke.com/search"

def get_joke():
    response = requests.get(url, headers={"Accept": "application/json"})
    data = response.json()

    rand_num = random.randint(0,10)
    print(data["results"][rand_num]["joke"])

get_joke()
