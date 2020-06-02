from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv



session = HTMLSession()
r = session.get("https://www.mitel.com/find-a-partner?loc=04330&dist=300")
r.html.render(wait=3.0, keep_page=True)

soup = BeautifulSoup(r.html.find("#mitel-results-section")[0].raw_html, "html.parser")



details = []
for result in soup.select("div.col-md-12.result--item.col-xs-12 > div"):
    details.append({
        "level": result.select("span:nth-child(1)")[0].text.strip(),
        "type": result.select("span:nth-child(2)")[0].text.strip(),
        "name": result.select("h6")[0].text.strip(),
        "loc": result.select("p")[0].text.strip(),
    })

with open('scraped.csv', 'a', newline='') as csvFile:

    csvWriter = csv.DictWriter(csvFile, ['level', 'type', 'name', 'loc'])
    csvWriter.writerows(details)
