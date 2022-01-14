import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request 
from urllib.error import URLError, HTTPError
import webbrowser as wb

import OpenWeb as op

all_URL_list = []
error_url404 = []
error_url403 = []
# 문자열 전처리 함수

def pre_str_setting():
    mixed_url_list = []
    url_list = []
    cnt = 0
    mixed_txt = open("MixedURLs.txt", "r")
    for line in mixed_txt:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        mixed_url_list.append(line_list)
    mixed_txt.close()
    
    for i, line in enumerate(mixed_url_list):
        if "https:" in mixed_url_list[i][-2]:
            add_url = mixed_url_list[i][-2]
            url_list.append(add_url)
        else:
            print("Can't find https")
        cnt = i
    print("Moving mixed to all : {} moved".format(cnt))
    
    file_all_urls = open("all_URLs.txt", "w")
    for line in url_list:
        file_all_urls.write(line + "\n")
    file_all_urls.close()
    print("Writing mixed_url --> all_url Done")

def read_URLs():
    """
    all_URLs.txt파일을 읽고 라인들을 모두 url_list에 저장해서 반환.
    """
    a_file = open("all_URLs.txt", "r")
    url_list = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        url_list.append(line_list[0])
    return url_list
    a_file.close()
    #print(all_URL_list)

def check_url(urls):
    for i, url in enumerate(urls):
        try:
            res = urllib.request.urlopen(url)
            print(i+1, res.status)
        except HTTPError as e:
            err = e.read()
            code = e.getcode()
            print("{} {} <--".format(i+1, code)) ## 404
            if code == 404:
                error_url404.append(url)
            else:
                error_url403.append(url)
            
def write_error_on_txt():
    textfile404 = open("link404.txt", "w")
    for line in error_url404:
        textfile404.write(line + "\n")
    textfile404.close()
    
    textfile403 = open("link403.txt", "w")
    for line in error_url403:
        textfile403.write(line + "\n")
    textfile403.close()
    
    print("Write Error done.")


def main():
    pre_str_setting() # 복붙한 정돈 안된 txt에서 url들만 추려서 all_URLs.txt에 정리하여 쓰기.
    all_URL_list = read_URLs()
    check_url(all_URL_list)
    
    # -------- info --------
    print("How many url: {}".format(len(all_URL_list)))
    print("How many 404: {}".format(len(error_url404)))
    print("How many 403: {}".format(len(error_url403)))
    print("first url : {}".format(all_URL_list[0]))
    print("last url : {}".format(all_URL_list[-1]))
    print("These are 404:\n", *error_url404, sep="\n")
    # -------- info --------
    
    write_error_on_txt()
    
    op.main()
    
main()