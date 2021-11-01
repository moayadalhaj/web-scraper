import requests
from bs4 import BeautifulSoup
import json

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    return len(citations)


def get_citations_needed_report(URL):
    all_tags = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    double = True
    for result in citations:
        if (result.parent.parent.parent.text.count('needed') == 1):
            all_tags.append(result.parent.parent.parent.text.split('[')[0])
        elif double == True:
            all_tags.append(result.parent.parent.parent.text.split('[')[0])
            double = False
        elif double == False:
            all_tags.append(result.parent.parent.parent.text.split('[')[1][17:])
            double = True
    file_content = json.dumps(all_tags)
    with open('all_citations.json', 'w') as file:
        file.write(file_content)
    return '\n\n'.join(all_tags)


if __name__ == "__main__":
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))