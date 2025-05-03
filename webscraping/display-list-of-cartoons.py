import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    #myHeaders = {
    #        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Ubuntu; Linux x86_64; rv:109.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    #}
    myHeaders = {      
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }

    search_url = ("https://www.imdb.com/list/ls005121870")
    get_source_code_response = requests.get(search_url, headers=myHeaders)
    response_content = get_source_code_response.content

    global soup
    soup = BeautifulSoup(response_content, features="html.parser")
    for data in soup(['h3', 'class']):
        plaintext = data.get_text()
        matchone = re.search(r"More to explore", plaintext)
        matchtwo = re.search(r"Recently viewed", plaintext)
        if matchone:
            continue
        if matchtwo:
            continue
        print(data.get_text())
