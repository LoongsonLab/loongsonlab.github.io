import os
import re

def replace_string_in_folder(path, old_string, new_string):
    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            chinese_name = get_chinese_name_from_file(folder_name)
            print(chinese_name)
            if chinese_name:
                replace_string_in_files(folder_path, old_string, new_string, chinese_name)

def get_chinese_name_from_file(folder_name):
    print(folder_name)
    name_file_path = './name_en.txt'
    print(name_file_path)
    if os.path.isfile(name_file_path):
        with open(name_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            match = re.search(folder_name + r',\s*(.*)', content)
            if match:
                comma_contents = match.group(1)
                return comma_contents.strip()            
    return None

def replace_string_in_files(folder_path, old_string, new_string, chinese_name):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_string_in_file(file_path, old_string, new_string, chinese_name)

def replace_string_in_file(file_path, old_string, new_string, chinese_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        replaced_content = content.replace(old_string, chinese_name)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(replaced_content)

# 设置路径和要替换的字符串
path = '/Users/zhaodongru/Documents/loongsonlab/_people'  # 将此处替换为实际的路径
old_string = 'Dongru Zhao'  # 要替换的字符串

# 调用函数来遍历文件夹并替换字符串
replace_string_in_folder(path, old_string, '')

