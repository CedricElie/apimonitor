# Creating this code I wanted something real quick to test http url reacheability
# Written by: @CedricElie, on Sun 28 Aug 2022
# Feel free to update it

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sites = ["http://www.google.com","http://www.twitter.com","https://192.168.11.11"]

for item in sites:
    try:
        r = requests.get(item, verify=False, timeout=1)
        rcode = r.status_code
        if rcode == 200:
            print( item + ": API is up")
        else:
            print(item + ": API is down")
    except requests.exceptions.ConnectionError as conn:
        print(item + ": Is unreachable or down")
    except requests.exceptions.ConnectTimeout as timeout:
        raise SystemExit(timeout)
        print(item + ": Down timeout")
    except requests.exceptions.ReadTimeout as readout:
        #raise SystemExit(readout)
        print(item + ": Read timeout, host is unreachable")
