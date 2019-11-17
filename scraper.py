import requests
from lxml import html

USERNAME = 'tnetwork'
PASSWORD = '1dehudaa'

LOGIN_URL = 'https://www.centraldispatch.com/'
URL = 'https://www.centraldispatch.com/protected/cargo/dispatched-to-me?folder=Dispatched'

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='CSRFToken']/@value")))[0]

    #Create Payload
    payload =  {
        "Username": USERNAME,
        "Password": PASSWORD,
        "CSRFToken": authenticity_token
    }

    #Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer =LOGIN_URL))

    #Scrape url
    print('success')

if __name__ == '__main__':
    main()