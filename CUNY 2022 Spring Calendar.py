from dataclasses import dataclass
from bs4 import BeautifulSoup
import urllib.request

#2022 Spring Semester Academic Calendar
def main():
    URL = 'https://sps.cuny.edu/academics/academic-calendar/2021-2022-calendar/spring-2022'

    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, 'html.parser')

    table_list = soup.find("tbody")
    date_list = table_list.find_all("tr")

    data_lists = []

    for i in date_list:
        data_lists.append(i.get_text())


    date_lists_length = len(data_lists)

    #print(type(date_list_length))


    for i in range(date_lists_length):
        print(data_lists[i])


if __name__ == "__main__":
    main()