from gettext import find
import numpy as np
import requests
from bs4 import BeautifulSoup
import urllib.request 
from urllib.error import URLError, HTTPError
import OpenWeb as op
from urllib.parse  import quote
import re

all_URL_list = []
url200 = []
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
        cnt = i + 1
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
        cnt = i + 1
        if i < 10:
            cnt = str(cnt).zfill(2)
        else:
            pass
        try:
            header = {'User-Agent' : 'Chrome/97.0.4692.71'}
            req = urllib.request.Request(url, headers=header)
            res = urllib.request.urlopen(req)
            
            if res.status == 200:
                print("  {} {}".format(cnt, res.status))
                url200.append(url)
            else:
                print("  {} {}, non 200 <--".format(cnt, res.status))
        except HTTPError as e:
            err = e.read()
            code = e.getcode()
            print("  {} {} <--".format(cnt, code)) ## 404, 403, etc
            if code == 404:
                error_url404.append(url)
            else:
                error_url403.append(url)
                
        except UnicodeEncodeError as ue:
            print("UnicodeEncodeError found.")
            try:
                find_kor = re.compile('[가-힣]+').findall(url)
                print(cnt, find_kor[0], "has been quoted.")
                query = quote(find_kor[0])
                url = url.replace(find_kor[0], query)
                req = urllib.request.Request(url, headers=header)
                res = urllib.request.urlopen(req)
                if res.status == 200:
                    print("  {} {}".format(cnt, res.status))
                    url200.append(url)
                else:
                    print("{} {}<-- UnicodeEncodeError".format(cnt, url))
                    error_url403.append(url)
            except:
                print("{} {}<-- UnicodeEncodeError".format(cnt, url))
                print(url.encode('utf8'))
                error_url403.append(url)
                pass
            
            
def write_error_on_txt():
    textfile404 = open("link404.txt", "w")
    for line in error_url404:
        textfile404.write(line + "\n")
    textfile404.close()
    
    textfile403 = open("link403.txt", "w")
    for line in error_url403:
        textfile403.write(line + "\n")
    textfile403.close()
    
    textfile200 = open("link200.txt", "w")
    for line in url200:
        textfile200.write(line + "\n")
    textfile200.close()
    
    print("Write 200 & Error done.")


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
    
main()
op.main()