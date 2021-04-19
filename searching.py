import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    for a in file_name:
        if field == a:
            return None

    # if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
    #     return None

    file = file_name

    with open("sequential.json") as file_name:
        slovniky = json.load(file_name)

    s = slovniky[field]
    return s


def linear_search(s,hledane_cislo):
    index = []
    count = 0
    for position, a in enumerate(s):
        if a == hledane_cislo:
            index.append(position)
            count += 1

    dict ={
        "position": index,
        "count": count

    }

    return dict


def pattern_search(sekvence, vzor):
    delka = len(vzor)
    position = set()
    start_index = 0
    posledni_index = delka

    for index, i in enumerate(sekvence):
        if vzor == sekvence[index:index+delka]:
            position.add(index + delka // 2)


    return position

def main():
    file = "sequential.json"
    s = read_data(file, "unordered_numbers")
    r = linear_search(s, hledane_cislo=0)
    s_2 = read_data(file, "dna_sequence")
    p = pattern_search(s_2,"ATA")
    print(p)


if __name__ == '__main__':
    main()