import requests
import time

url = 'https://epaper.timesgroup.com/mirror/bangalore'
url1 = 'https://deadmau5.com/'

while True:
    try:
        response = requests.get(url)
        response1 = requests.get(url1)
        if response.status_code == 200 and response1.status_code == 200:
            print('Websites archived successfully!')
        else:
            print(f'An error occurred: {response.status_code} and {response1.status_code}')
        time.sleep(8640)
    except Exception as e:
        print(f'An exception occurred: {e}')