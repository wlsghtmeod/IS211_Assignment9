from bs4 import BeautifulSoup
import urllib.request

#Top 5 news headlines of NYT
def main():
    URL = 'https://www.nytimes.com'

    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, 'html.parser')

    h3_list = soup.find_all("h3")

    h3_lists = []

    for h3 in h3_list:
        h3_lists.append(h3.get_text())

    num = 1
    for i in h3_lists[:5]:
        print(f"{num}: {i}")
        num += 1


if __name__ == "__main__":
    main()