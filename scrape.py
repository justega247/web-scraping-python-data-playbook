import requests
import re
from bs4 import BeautifulSoup


PAGE = "http://localhost:8000/auto_mpg.html"

result = requests.get(PAGE)

# print(type(result))
# print(result.status_code)

# rb = requests.get(PAGE + "X")  # returns an error
#
# rb.raise_for_status()

# returned = result.content[:10]
#
# print(returned)
# print(type(result.content))

source = result.text

# print(type(source))

soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())
# print(soup.prettify()[:300])

# print(soup.title)
# print(soup.title.get_text())
# print(soup.title.text)

# print(soup.html.head == soup.head)

# print(soup.head.parent.name)

# print(soup.body.text[:1000])

# print(soup.body.h1)
# print(soup.body.p)
# print('lol', soup.body.h1.next_sibling)  # next sibling here is a newline character '\n'
# print(soup.body.h1.next_sibling.next_sibling)

# print(soup.body.a.attrs)

# print(soup.body.a.attrs['href'])

# print(soup.find_all('a'))
# print(soup.find_all('a')[0])
# print(type(soup.find_all('a')[0]))

# print(soup.find(id='car-2'))
# print(type(soup.find(id='car-2')))
# print(soup.find(id='car-0'))
# print(soup.find(id='car-0') is None)

# print(soup.find_all('div', class_='car_block'))
# print(len(soup.find_all('div', class_='car_block')))

div = soup.find_all('div', class_='car_block')[0]
# print(div.prettify())

# print(div.text)
# print(list(div.stripped_strings))

# print(div.find_all('span'))
#
# print(div.find('span', class_='mpg'))
# print(div.find('span', class_='mpg').text)

# print(re.findall('.* cubic inches', div.text))
# print(re.findall('.* \d+.\d+ cubic inches', div.text))
# print(re.findall('.* (\d+.\d+) cubic inches', div.text))

# print(soup.find_all('span', class_='mpg'))
# print(list(mpg.text for mpg in soup.find_all('span', class_='mpg')))

# print(soup.select('#car-1 > span.mpg'))  # Using selector gotten from chrome dev tool

# car_blocks = soup.find_all('div', class_='car_block')
# print(len(car_blocks))
