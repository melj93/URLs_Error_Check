import urllib.request 
from urllib.error import URLError, HTTPError

all_URL_list = []
error_url = []

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
    print("These are 404:", error_url)
            
def write_error_on_txt():
    textfile = open("link404.txt", "w")
    for line in error_url:
        textfile.write(line + "\n")
    textfile.close()
    print("Write Error done.")

def main():
    all_URL_list = read_URLs()
    check_url(all_URL_list)
    # write_error_on_txt()
    
main()