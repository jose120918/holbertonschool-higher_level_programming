#!/usr/bin/python3
'''module append_after'''


def append_after(filename="", search_string="", new_string=""):
    '''
    function append_after
    '''
    with open(filename, encoding="utf-8") as file:
        lines = []
        while True:
            line = file.readline()
            if not line:
                break
            lines.append(line)
            if line.find(search_string) != -1:
                lines.append(new_string)
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(lines)
