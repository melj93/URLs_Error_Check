from os import sep
import webbrowser as wb

urls = [] # Web에서 Open할 urls
"""
너무 많은 url을 열면 좀 부담스러워서
조건문: 아래 txt_to_url_list() i > 20
으로 갯수를 정하고 있음.
input으로 갯수 값을 받아서 수정하는 방안으로 갈거임.
"""
file_name_dict = {"404" : "link404", 
             "403" : "link403",
             "200" : "link200",
             "ne" : "all_URLs"
             }

def txt_to_url_list(file_name):
    """파일 열고, 
    url_list에 Insert text line by line, 
    20번 넘을시 20번넘었다는 bool값에 True넣고 종료.
    """
    bool_20 = False
    with open("{}.txt".format(file_name), "r") as a_file:
        print("{}file openned.".format(file_name))
        url_list = []
        for i, line in enumerate(a_file):
            if i > 9:
                print("url {} openned.".format(i))
                bool_20 = True
                break
            stripped_line = line.strip()
            line_list = stripped_line.split()
            url_list.append(line_list[0])
        
        a_file.close()
        print("bool : {}, 20 more urls".format(bool_20))
        return url_list, bool_20

def open_urls(urls: list):
    for i, url in enumerate(urls):
        wb.open(url)
        
def delte_lines(file_name, urls):
    """앞에 읽은 url들 txt파일에서 삭제하고 저장하는 함수. 읽은 만큼 지우기."""
    cnt_d  = 0 # count deleted line.
    numb_d = len(urls) # 지울 url 갯수
    print("Delete lines activated", file_name)
    file_to_edit = open("{}.txt".format(file_name), "r")
    lines = file_to_edit.readlines()
    file_to_edit.close()
    
    file_edit = open("{}.txt".format(file_name), "w")
    for i, line in enumerate(lines): 
        if i < len(urls): # pass해서 지우고, else에서 덮어씀.
            cnt_d = i + 1
            pass
        else:
            file_edit.write(line)
        
    file_edit.close()
    print("Deleted {} lines.".format(cnt_d))
    print("{} lines remain.".format(len(lines) - cnt_d)) # Count remainning lines

def main():
    bool_20 = False
    file_name = input("Choice one [200, 404, 403, ne] :")
    if file_name == "no":
        print("Terminating OpenWeb")
        return
    # 키를 입력받아 값을 str로 저장해서 함수에 넣어야함
    file_name_val = file_name_dict['{}'.format(file_name)]
    urls, bool_20 = txt_to_url_list(file_name_val)
    print("last bool: {}".format(bool_20))
    open_urls(urls) # url 열기 20개 단위로.
    
    if bool_20 == True: # 읽은 
        delte_lines(file_name_val, urls)
    else:
        pass