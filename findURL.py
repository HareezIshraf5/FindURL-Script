import re
import urllib.request
from urllib.parse import urlparse, urlsplit
import sys


url = sys.argv[1]

def findURL(url):
    # Extracting TLD
    tld = urlsplit(url).hostname.split('.')[-1]
    print("TLD:", tld)
    
    # Extracting Domain
    parsed_url = urlsplit(url)
    domain = ".".join(parsed_url.hostname.split(".")[-2:])

    print("DOMAIN:", domain)
    
    # Extracting hostname
    hostname = urlparse(url).hostname
    print("HOSTNAME:", hostname)

    # Extracting path
    path = urlparse(url).path
    print("PATH:", path)
    
    # Extracting protocol
    protocol = urlparse(url).scheme
    print("PROTOCOL:", protocol)

    # Extracting links
    links = []
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
        links = re.findall(r'href=[\'"]?([^\'" >]+)', html)
    print("LINKS:")
    
    same_hostname = []
    same_domain = []
    diff_domain = []
    for link in links:
        if hostname in link:
            same_hostname.append(link)
        elif domain in link:
            same_domain.append(link)
        else:
            diff_domain.append(link)
    if same_hostname:
        print("Same hostname:")
        for link in same_hostname:
            print("\t", link)
    if same_domain:
        print("Same domain:")
        for link in same_domain:
            print("\t", link)
    if diff_domain:
        print("Different domain:")
        for link in diff_domain:
            print("\t", link)

findURL(url)
# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Please enter the URL like this: python yourscript.py URL")
#         sys.exit()
#     findURL(sys.argv[1])
