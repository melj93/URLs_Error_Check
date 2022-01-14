from os import sep
import webbrowser as wb

urls = []
file_name_dict = {"404" : "link404", 
             "403" : "link403",
             "200" : "link200",
             "ne" : "all_URLs"
             }

def txt_to_url_list(file_name):
    bool_20 = False
    with open("{}.txt".format(file_name), "r") as a_file:
        print("{}file openned.".format(file_name))
        url_list = []
        for i, line in enumerate(a_file):
            if i > 20:
                print("url {} openned.".format(i - 1))
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
        
def delte_20lines(file_name):
    print("delete 20 lines activated")
    file_to_edit = open("{}.txt".format(file_name), "r")
    lines = file_to_edit.readlines()
    file_to_edit.close()
    
    print(lines)
    
    file_edit = open("{}.txt".format(file_name), "w")
    for i, line in enumerate(lines):
        print("{} --- {}".format(line, urls[i]))
        # if line in lines:
        #     file_edit.write(line)
    file_edit.close()

def main():
    bool_20 = False
    file_name = input("Choice one [200, 404, 403, ne] :")
    if file_name == "no":
        print("Terminating OpenWeb")
        return
    # 키를 입력받아 값을 str로 저장해서 함수에 넣어야함
    val = file_name_dict['{}'.format(file_name)]
    urls, bool_20 = txt_to_url_list(val)
    print("last bool: {}".format(bool_20))
    if bool_20 == True:
        delte_20lines(file_name)
    else:
        pass
    # open_urls(urls)
#main()

ex_url = [
    "https://kpopmart.com/bigbang/2855-bigbang-arttoy-sticker.html", 
"https://kpopmart.com/bigbang/2879-5845-bigbang-krunk-x-bigbang-baebae-ver.html#/455-bigbang-daesung",
"https://kpopmart.com/bigbang/2880-5849-bigbang-krunk-x-bigbang-baebae-ballpen.html#/455-bigbang-daesung",
"https://kpopmart.com/bigbang/2890-bigbang-made-ballpen-set-monami-153.html", 
"https://kpopmart.com/bigbang/2893-5856-bigbang-copy.html#/455-bigbang-daesung", 
"https://kpopmart.com/bigbang/2904-bigbang-copy.html", 
"https://kpopmart.com/bigbang/2912-5896-bigbang-copy.html#/28-ver-a",
"https://kpopmart.com/bigbang/2943-bigbang-made-shower-curtain.html",
"https://kpopmart.com/bigbang/2951-5932-bigbang-made-jacket.html#/2-size-m",
"https://kpopmart.com/bigbang/2957-bigbang-made-strap-bracelet.html",
"https://kpopmart.com/bigbang/2969-5958-bigbang-made-t-shirts-vermade.html#/2-size-m",
"https://kpopmart.com/bigbang/2976-bigbang-copy.html",
"https://kpopmart.com/bigbang/2983-bigbang-copy.html",
"https://kpopmart.com/bigbang/2986-bigbang-copy.html",
"https://kpopmart.com/bigbang/2989-bigbang-copy.html",
"https://kpopmart.com/bigbang/2993-bigbang-10th-bigbang-weekly-planner.html",
"https://kpopmart.com/bigbang/2995-bigbang-copy.html",
"https://kpopmart.com/bigbang/3009-bigbang-10th-bigbang-coloring-book.html",
"https://kpopmart.com/bigbang/3013-bigbang-10th-bigbang-pencil-set.html",
"https://kpopmart.com/bigbang/3031-bigbang-10th-bigbang-pocket-blanket.html",
]

file_to_edit = open("{}.txt".format("link200"), "r")
lines = file_to_edit.readlines()
file_to_edit.close()

file_edit = open("{}.txt".format("link200"), "w")
cnt_d  = 0
cnt_r = 0
for i, line in enumerate(lines):
    if i < 20:
        print("Delete line, {}".format(i+1))
        cnt = i + 1
        pass
    else:
        print("Write lines again.".format(i+1))
        file_edit.write(line)
    
file_edit.close()
print("Deleted {} lines.".format(cnt_d))
print("{} lines remain.".format(cnt_r))