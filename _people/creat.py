import os
import shutil

def create_folders_from_file(path, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            folder_name = line.strip()
            folder_path = os.path.join(path, folder_name)
            try:
                os.makedirs(folder_path)
                print(f"创建文件夹: {folder_path}")
            except FileExistsError:
                print(f"文件夹已存在: {folder_path}")
            
            # 复制文件并替换特定字符串
            source_file_en = './index.en.md'  # 要复制的英文文件
            source_file_zh = './index.zh.md'  # 要复制的中文文件
            target_file_en = os.path.join(folder_path, 'index.en.md')
            target_file_zh = os.path.join(folder_path, 'index.zh.md')

            shutil.copyfile(source_file_en, target_file_en)
            shutil.copyfile(source_file_zh, target_file_zh)

            # 使用文件夹名替换特定字符串
            replace_string_in_file(target_file_en, folder_name)
            replace_string_in_file(target_file_zh, folder_name)

def replace_string_in_file(file_path, folder_name):
    with open(file_path, 'r+') as file:
        content = file.read()
        replaced_content = content.replace('zhaodongru', folder_name)
        file.seek(0)
        file.write(replaced_content)
        file.truncate()

# 设置路径和文件名
path = '/Users/zhaodongru/Documents/loongsonlab/_people'  # 将此处替换为你想要创建文件夹的路径
file_path = '/Users/zhaodongru/Documents/loongsonlab/_people/name.txt'  # 将此处替换为包含文件夹名称的文件的路径

# 调用函数来创建文件夹并复制文件
create_folders_from_file(path, file_path)

