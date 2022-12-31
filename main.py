import requests
import selectorlib
import time
import smtplib, ssl
import os



url = 'http://programmer100.pythonanywhere.com/tours/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url = url, headers=HEADERS)
    print()
    print('------------------------------------------------------------')
    print(f'Extracting data from URL: {response.url}')
    print('------------------------------------------------------------')
    
    text = response.text
    # print(f"Response.text{text}")
    return text


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    print(f"Value: {value}")
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "zafrip14@gmail.com"
    password = "lroyqtbeghgwydpn"

    receiver = "zafrip14@gmail.com"
    context = ssl.create_default_context()

    # msg = 'Subject: {}\n\n{}'.format('Tours', message)


    msg = f"Subject: Tours\n".encode('utf-8') + message.encode('utf-8')

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr= username, to_addrs=receiver, msg=msg)



def read_tours_list():
    with open('tours_list.txt', 'r') as file:
        tours_list = file.readlines()
    tours_list = [tour.replace('\n','') for tour in tours_list]
    return tours_list        


def add_tours(tours):
    with open('tours_list.txt', 'a') as file:
        print(f"Writing list: {tours}")
        file.writelines(tours+'\n')



if __name__ == '__main__':
    count = 1
    while count <= 10:
        scraped = scrape(url)
        extracted = extract(scraped)
        print(extracted)
        if extracted != 'No upcoming tours':
            tours_list = []
            tours_list = read_tours_list()
            print(f'Reading Tours List: {tours_list}')
            if extracted not in tours_list:
                add_tours(extracted)
                send_email(message=extracted)
        else:
            print('No email')
        time.sleep(1)
        count += 1

