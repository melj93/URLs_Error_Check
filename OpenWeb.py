import webbrowser as wb

urls = []
error_code: int = 404 # 열고싶은 파일 에러코드를 적으시오.

def txt_to_url_list():
    a_file = open("link{}.txt".format(error_code), "r" )
    url_list = []
    for i, line in enumerate(a_file):
        stripped_line = line.strip()
        line_list = stripped_line.split()
        if line_list[0][:1] == "#":
            print("403 url {} openned.".format(i))
            break
        print(i, line_list[0])
        url_list.append(line_list[0])
    return url_list
    a_file.close()

def open_urls(urls: list):
    for i, url in enumerate(urls):
        wb.open(url)

urls = txt_to_url_list()

open_urls(urls)