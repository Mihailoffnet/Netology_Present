# all_files_dict ={}
files = ['1.txt', '2.txt', '3.txt']

def great_dict(file_name_list):
    all_files_dict ={}
    for file_name in file_name_list:
        with open(file_name, 'r') as f:
            file_list = f.readlines()
        len1 = len(file_list)
        file_list.insert(0, f'{len(file_list)}\n')
        file_list.insert(0, f'{file_name}\n')
        all_files_dict[len1] = file_list
    result = dict(sorted(all_files_dict.items(), key=lambda x: x[0]))
    return result

all_files_dict_sorted = great_dict(files)

with open('final.txt', 'x', encoding = 'UTF-8') as file:
    for values in all_files_dict_sorted.values():
        file.writelines(values)
        file.write('\n')

