from bs4 import BeautifulSoup
from urllib.request import urlopen


# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"


class ParseTableFromUrl:
    def __init__(self, url):
        self.url = url

    def parse_url(self):
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup

    def get_table_data(self):
        table = self.parse_url().find("table")
        data = []
        for row in table.find_all("tr"):
            data.append([td.text for td in row.find_all("td")])
        data.pop(0)
        return data

    @staticmethod
    def get_max_element_in_position(data, position):
        return max([int(row[position]) for row in data])

    def draw_empty_grid(self, data):
        max_x = self.get_max_element_in_position(data, 0)
        max_y = self.get_max_element_in_position(data, 2)
        empty_grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        return empty_grid

    def get_2d_grid(self):
        table_data = self.get_table_data()
        grid = self.draw_empty_grid(table_data)
        for row in table_data:
            x = int(row[0])
            y = int(row[2])
            grid[y][x] = row[1]
        return reversed(grid)

    def print_secret_message(self):
        grid = self.get_2d_grid()
        message = ""
        for row in grid:
            message += ''.join(symb for symb in row)
            message += '\n'
        print(message)



# table_data = parse_url(url)
# print(table_data)
# table_data = [['0', '█', '0'], ['0', '█', '1'], ['0', '█', '2'], ['1', '▀', '1'], ['1', '▀', '2'], ['2', '▀', '1'], ['2', '▀', '2'], ['3', '▀', '2']]
table_data = [['0', '█', '0'], ['0', '█', '1'], ['0', '█', '2'], ['0', '█', '3'],
              ['2', '▀', '3'], ['3', '▀', '2'], ['4', '▀', '1'], ['5', '▀', '0'],
              ['6', '▀', '1'], ['7', '▀', '2'], ['8', '▀', '3']]


ms = ParseTableFromUrl(url)
ms.print_secret_message()

