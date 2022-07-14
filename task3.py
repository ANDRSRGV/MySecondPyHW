

file_set = ['1.txt', '2.txt', '3.txt']
sub_dir='SortedFiles/'
file_len = []
file_len_name = {}
for file in file_set:
    with open(sub_dir + file,'r', encoding='utf-8') as data:
        text = data.read()
        lines = text.count('\n') + 1
        file_len.append(lines)
        file_len_name.setdefault(lines,[])
        file_len_name[lines].append(file)
print(file_len)
file_len.sort()
print(file_len)
print(file_len_name)

output = ''
with open(sub_dir + 'sorted_files.txt','w', encoding='utf-8') as data:
    for file_pos in file_len:
        for file in file_len_name[file_pos]:
            output += f'{file}\n{file_pos}\n'
            with open(sub_dir + file, 'r', encoding='utf-8') as cur_file:
                output += f'{cur_file.read()}\n\n'
    data.write(output)


