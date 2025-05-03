import requests
from bs4 import BeautifulSoup

def getPageContents(url):
    myHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(url, headers=myHeaders)
    
    #List Return Objects Methods
    #print(dir(page))

    if page.status_code == 200:
        return page.text
    return None

def getQuotesAndAuthors(pageContents):
    soup = BeautifulSoup(pageContents, 'html.parser')
    try:
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
    except Exception as e:
        print(e)
        return None, None
    return quotes, authors

try:
    if __name__ == "__main__":
        pageContents = getPageContents("https://quotes.toscrape.com")
        if pageContents:
            quotes, authors = getQuotesAndAuthors(pageContents)
            for i in range(len(quotes)):
                print(quotes[i].text)
                print(authors[i].text)
                print()
except Exception as er:
    print("Exception: Page content variable did not receive any contents!")
    print(er)
