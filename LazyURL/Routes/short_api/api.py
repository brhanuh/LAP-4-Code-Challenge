import requests
import json
from dotenv import load_dotenv
from os import environ

load_dotenv()
api_key = environ.get('SECRET_API_KEY')



def api_shorten(long_url):

    # url = f"https://api.short.io/domains/"
    # payload = json.dumps({"hideReferer":False,"httpsLinks":False,"hostname":"lazyurl.com","linkType":"random"})
    # headers = {
    #     'accept': "application/json",
    #     'content-type': "application/json",
    #     'authorization': api_key
    # }

    # response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)
    print("Long url", long_url)
    res = requests.post('https://api.short.io/links', {
        'domain': 'lazyurl.com',
        'originalURL': 'www.google.com',
    }, headers = {
        'authorization': 'sk_E4vkZyGkYUzNHxe5',
        'content-type': 'application/json'
    }, json=True)

    print(res)

    res.raise_for_status()
    data = res.json()

    print(data)




