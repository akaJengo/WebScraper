from lxml import html 
import requests

def main():
    sign_in = '<URL>'

    #Starts Session
    session_requests = requests.session()

    #Auth
    result = session_requests.get(sign_in)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]
    
    #The Payload
    EMAIL = "<USER_EMAIL>"
    PASSWORD = "<PASSWORD>"

    payload = {
        "user[email]": EMAIL, 
        "user[password]": PASSWORD, 
    }

    #Login Phase, this is where shit hits the fan
'''
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
'''

    result = session_requests.post(
        sign_in, 
        data = payload, 
    )
    #DEBUG Content print(result.content)
    print(result.ok) #If true, result was successful
    print(result.status_code)


    #Content Scrape, this is the easy part
    url = '<URL OF SCRAPE>'
    result = session_requests.get(
        url, 
        headers = dict(referer = url)
    )

    tree = html.fromstring(result.content)
    prices = tree.xpath('//span[@class ="livetrading-stats-dollarpnl"]/text()')
    print('Prices', prices)



main()