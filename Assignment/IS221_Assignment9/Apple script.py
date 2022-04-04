from bs4 import Beautifulsoup
import requests


def main():
    URL = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

    html = requests.get(URL)
    soup = Beautifulsoup(html.content, 'html5lib')

    print(soup)


if __name__ == "__main__":
    main()