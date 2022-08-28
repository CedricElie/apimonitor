# Creating this code I wanted something real quick to test http url reacheability
# Written by: @CedricElie, on Sun 28 Aug 2022
# Feel free to update it

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sites = ["http://www.google.com","http://www.twitter.com","https://ebanking.afrilandfirstbank.com/particuliers/index.ebk"]

for item in sites:

    r = requests.get(item,verify=False)
    rcode = r.status_code
    try:
        if rcode == 200:
            print( item + ": API is up")
        else:
            print(item + ": API is down")
    except requests.exceptions.ConnectionError as err:
        print(item + ": Down connection error")
    except requests.exceptions.ConnectTimeout as e:
        raise SystemExit(e)
        print(item + ": Down timeout")
