from os import sep
import webbrowser as wb

urls = []

file_name_dict = {"e404" : "link404", 
             "e403" : "link403",
             "ne" : "all_URLs"
             }

def txt_to_url_list(file_name):
    a_file = open("{}.txt".format(file_name), "r")
    print("{}file openned.")
    url_list = []
    for i, line in enumerate(a_file):
        if i == 20:
            print("url {} openned.".format(i))
            break
        stripped_line = line.strip()
        line_list = stripped_line.split()
        print(i, line_list[0])
        url_list.append(line_list[0])
    return url_list
    a_file.close()

def open_urls(urls: list):
    for i, url in enumerate(urls):
        wb.open(url)

def main():
    file_name = input("Choice one [e404, e403, ne] :")
    print(file_name)
    # 키를 입력받아 값을 str로 저장해서 함수에 넣어야함
    val = file_name_dict['{}'.format(file_name)]
    urls = txt_to_url_list(val)
    open_urls(urls)
    
main()