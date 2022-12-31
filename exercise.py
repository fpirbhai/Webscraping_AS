import requests
import selectorlib
import datetime
import time
import pandas
import os


URL = 'http://programmer100.pythonanywhere.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
SLEEP = 60
DURATION = 600
ITERATION = int(DURATION/SLEEP)

def scrape(url):
    response = requests.get(url = url, headers=HEADERS)
    return response.text


def extract_info(source_code):
    extract_data = selectorlib.Extractor.from_yaml_file('extract_temp.yaml')
    value = extract_data.extract(source_code)['temp']
    return value


def write_data(dat, format='csv', filename = 'temp.'):
    # Check if file exist. Create the file with headers
    if not os.path.exists(filename+format):
        with open(filename+format,'a') as file:
            file.writelines('date,temperature\n')

    # 1. Check if header is available
    # 2. Add dates and temperature...
    with open(filename+format,'r+') as file:
        temp = file.readlines()
        if len(temp) == 0:
            file.writelines('date,temperature\n')
        file.writelines(dat)


if __name__ == '__main__':
    scraped = scrape(URL)

    count = 1
    while count <= ITERATION:
        value = extract_info(scraped)
        count += 1
        today_date = datetime.datetime.now()
        write_data(today_date.strftime('%d/%m/%Y %H:%M:%S')+ ',' + str(value)+'\n')
        time.sleep(SLEEP)



