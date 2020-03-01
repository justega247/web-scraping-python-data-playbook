import requests

result_1 = requests.get('https://en-gb.wordpress.org/plugins/browse/popular/')

with open('wordpress.html', 'w') as f:
    f.write(result_1.text)

#########################

result_2 = requests.get('https://hansard.parliament.uk/search/Members?currentFormerFilter=1&house=Commons')

with open('hansard.html', 'w') as f:
    f.write(result_2.text)
