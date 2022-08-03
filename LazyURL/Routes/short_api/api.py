import requests
import json
from dotenv import load_dotenv
from os import environ

load_dotenv()
api_key = environ.get('SECRET_API_KEY')



def api_shorten(long_url):

    url = "https://api.short.io/links"

    payload = {
        "allowDuplicates": False,
        "originalURL": long_url,
        "domain": "lazyurl.com"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "sk_E4vkZyGkYUzNHxe5"
    }

    response = requests.post(url, json=payload, headers=headers)

    result = response.json()

    return result['path']

    # url = f"https://api.short.io/domains/"    
    # payload = json.dumps({"hideReferer":False,"httpsLinks":False,"hostname":"lazyurl.com","linkType":"random"})
    # headers = {
    #     'accept': "application/json",
    #     'content-type': "application/json",
    #     'authorization': api_key
    # }

    # response = requests.request("POST", url, data=payload, headers=headers)

    # print(response.text)
    # print("Long url", long_url)
    # res = requests.post('"https://api.short.io/api/links?domain_id=489927&limit=30"', {
    #     'domain': 'lazyurl.com',
    #     'originalURL': 'https://github.com/getfutureproof/fp_guides_wiki/wiki',
    # }, headers = {
    #     'authorization': 'sk_E4vkZyGkYUzNHxe5',
    #     'content-type': 'application/json'
    # }, json=True)

    # print(res)

    # res.raise_for_status()
    # data = res.json()

    # print(data)




