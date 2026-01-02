from bs4 import BeautifulSoup
from urllib.request import urlopen

def parse_url(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    return soup

def get_table_data(url):
    table = parse_url(url).find("table")
    data = []
    for row in table.find_all("tr"):
        data.append([td.text for td in row.find_all("td")])
    data.pop(0)
    return data

def get_max_element_in_position(data, position):
    return max([int(row[position]) for row in data])

def draw_empty_grid(data):
    max_x = get_max_element_in_position(data, 0)
    max_y = get_max_element_in_position(data, 2)
    empty_grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    return empty_grid

def get_2d_grid(url):
    table_data = get_table_data(url)
    grid = draw_empty_grid(table_data)
    for row in table_data:
        x = int(row[0])
        y = int(row[2])
        grid[y][x] = row[1]
    return reversed(grid)

def print_secret_message_from_url(url):
    grid = get_2d_grid(url)
    message = ""
    for row in grid:
        message += ''.join(symb for symb in row)
        message += '\n'
    print(message)

url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
print_secret_message_from_url(url)