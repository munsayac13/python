import requests
import pandas as pd
from bs4 import BeautifulSoup


def display_text():
    myHeaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Ubuntu; Linux x86_64; rv:109.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    url = "https://www.skysports.com/premier-league-results/2025-04"
    get_source_code_response = requests.get(url, headers=myHeaders)
    response_content = get_source_code_response.content
    soup = BeautifulSoup(response_content, features="html.parser")

    # Displays more Rows
    #script = soup.select_one('[type="text/show-more"]')
    #script.replace_with(BeautifulSoup(script.contents[0], "html.parser"))

    # Test Stripping Html Text
    #print(soup.select(".fixres__item")[0].get_text(strip=True))
    #print(soup.select(".fixres__item")[0].get_text(strip=True, separator="|"))
    #print(soup.select(".fixres__item")[0].get_text(strip=True, separator="|").split("|")[:5])
    #print(soup.select(".fixres__item")[0].find_previous(class_="fixres__header2"))
    #print(soup.select(".fixres__item")[0].find_previous(class_="fixres__header2").get_text(strip=True))

    allData = []
    for item in soup.select(".fixres__item"):
        allData.append(item.get_text(strip=True, separator="|").split("|")[:5])
        allData[-1].append(
            item.find_previous(class_="fixres__header2").get_text(strip=True)
        )

    pandaDataFrame = pd.DataFrame(
        allData, columns=["Team 1", "Score 1", "Score 2", "Time", "Team 2", "Date"]
    )
    print(pandaDataFrame)

    # Display number each row
    #pandaDataFrame.to_csv("records.csv", index=True)
    pandaDataFrame.to_csv("records.csv", index=False)
    
if __name__ == "__main__":
    display_text()
