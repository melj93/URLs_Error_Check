import webbrowser as wb

urls = []

e404: str = "link404" # 열고싶은 파일 에러코드를 적으시오.
e403: str = "link403" 
ne: str = "all_URLs"
file_name = e403

def txt_to_url_list():
    a_file = open("{}.txt".format(file_name), "r")
    url_list = []
    for i, line in enumerate(a_file):
        stripped_line = line.strip()
        line_list = stripped_line.split()
        if line_list[0][:1] == "#":
            print("url {} openned.".format(i))
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