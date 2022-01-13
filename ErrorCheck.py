import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request 
from urllib.error import URLError, HTTPError

all_URL_list = []
error_url = []

# def extractURLs():  # 보완해야함
#     url: str = "https://api.fanarcade.net/admin/shop/product/?o=-1.-7&p=20"
#     response = requests.get(url)
#     #parse html
#     page = str(BeautifulSoup(response.content))
#     def getURL(page):
#         start_link = page.find("field-productUrl")
#         if start_link == -1:
#             return None, 0
#         start_quote = page.find('>', start_link)
#         end_quote = page.find('<', start_quote + 1)
#         url = page[start_quote + 1: end_quote]
#         return url, end_quote
    
    # while True:
    #     url, n = getURL(page)
    #     page = page[n:]
    #     if url:
    #         print(url)
    #     else:
    #         break

def read_URLs():
    a_file = open("all_URLs.txt", "r")
    url_list = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        url_list.append(line_list)
    return url_list
    a_file.close()
    #print(all_URL_list)

def check_url(urls):
    for i, url in enumerate(urls):
        try:
            res = urllib.request.urlopen(url[0])
            print(i, url[0], res.status)
        except HTTPError as e:
            err = e.read()
            code = e.getcode()
            print(i, url[0], code) ## 404
            error_url.append(url[0])
    print("These are 404:\n", *error_url, sep="\n")
            
def write_error_on_txt():
    textfile = open("link404.txt", "w")
    for line in error_url:
        textfile.write(line + "\n")
    textfile.close()
    print("Write Error done.")

def main():
    all_URL_list = read_URLs()
    how_many_url = str(np.shape(all_URL_list))
    print("How many url: {}".format(how_many_url))
    check_url(all_URL_list)
    how_many_404 = str(np.shape(error_url))
    print("How many 404: {}".format(error_url))
    
    write_error_on_txt()
    
main()