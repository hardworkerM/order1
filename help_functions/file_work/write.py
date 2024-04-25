

async def write_in(info):
    print('I AM IN WRITE_IN')
    file_name = 'user_all_text.txt'
    line = "; ".join(info) + '\n'
    with open(file_name, 'a', encoding='UTF-8') as file:
        file.write(line)


def read_out():
    file_name = 'user_all_text.txt'

    data = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            info = line.strip('\n')
            row=info.split('; ')
            row[0] = int(row[0])
            data.append(tuple(row))
    return data


def empty_file():
    file_name = 'user_all_text.txt'
    open(file_name, 'w').close()